from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,OrderDetail
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator
from django.db.models import Q

# FOR PAYMENT GATEWAY

from django.http import JsonResponse, HttpResponseServerError
from django.http.response import HttpResponseNotFound,JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
import logging
import stripe



# Create your views here.
def index(request):
    return render(request,'myapp/myapp.html')

def products(request):
    page_obj = products = Product.objects.all()
    
    product_name=request.GET.get('product_name')

    if product_name!='' and product_name is not None:
        page_obj=products.filter(name__icontains=product_name)


    paginator=Paginator(products,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj

    }
    return render(request,'myapp/index.html',context)




# class based view

class ProductListView(ListView):

    model=Product
    template_name='myapp/index.html'
    context_object_name='products'
    paginate_by=3

    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.GET.get('product_name')

        if product_name:
            queryset = queryset.filter(Q(name__icontains=product_name))

        return queryset




def product_detail(request,id):
    product =Product.objects.get(id=id)
    context={
        "product":product
    }
    return render(request,'myapp/detail.html',context)







@login_required
def add_product(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        image=request.FILES['upload']
        seller=request.user
        product=Product(name=name,price=price,desc=desc,image=image,seller=seller)
        product.save()
    return render(request,'myapp/addproduct.html')


# class based add view :

class ProductCreateView(CreateView):

    model=Product
    fields=['name','price','desc','image','seller']
    template_name='myapp/productcreate.html'
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)




@login_required
def update_product(request,id):
    product =Product.objects.get(id=id)
    if(request.method=='POST'):
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.desc=request.POST.get('desc')
        if 'upload' in request.FILES:
            product.image = request.FILES['upload']
        product.save()
        return redirect(f'/myapp/products/{id}')
    context={
        "product":product
    }
    return render(request,'myapp/updateproduct.html',context)





# class based view for Update view


class ProductUpdateView(UpdateView):

    model=Product
    fields=['name','price','desc','image','seller']
    template_name_suffix='_update_form'


@login_required
def delete_product(request,id):
    product =Product.objects.get(id=id)
    if(request.method=='POST'):
        if 'Delete' in request.POST:
            product.delete()
            return redirect('/myapp/products/')
        elif 'Cancel' in request.POST:
            return redirect('/myapp/products/') 
    context={
        "product":product
    }
    return render(request,'myapp/deleteproduct.html',context)

# class based view for delete:

class ProductDelete(DeleteView):
    model=Product
    template_name_suffix='_confirm_delete'
    success_url=reverse_lazy('myapp:products')


@login_required
def my_listings(request):
    products = Product.objects.filter(seller=request.user)
    context={
        'products':products
    }
    return render(request,'myapp/mylistings.html',context)




### payment through stripe


# class based detailed view:

class ProductDetailView(DetailView):
    model=Product
    template_name='myapp/detail.html'
    context_object_name='product'
    pk_url_kwargs='pk'

    def get_context_data(self, **kwargs):
        context=super(ProductDetailView,self).get_context_data(**kwargs)
        context['stripe_publishable_key']=settings.STRIPE_PUBLISHABLE_KEY
        return context

@csrf_exempt
def create_checkout_session(request, id):
    """
    Create a Stripe checkout session for a product.

    Args:
        request (HttpRequest): The request object.
        id (int): The product ID.

    Returns:
        JsonResponse: A JSON response with the checkout session ID.
    """
    product = get_object_or_404(Product, pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Create a Stripe checkout session
    checkout_session = stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),  # Convert to cents
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('myapp:success')) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('myapp:failed')),
    )

    # Create an order detail instance
    order = OrderDetail()
    order.customer_username = request.user.username
    order.product = product
    order.stripe_payment_intent = checkout_session['id']
    order.price = int(product.price * 100)  # Convert to cents
    order.save()

    # Return the checkout session ID as a JSON response
    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name='myapp/payment_success.html'

    def get(self, request, *args, **kwargs):
        session_id=request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()        
        session=stripe.checkout.Session.retrieve(session_id)
        stripe.api_key=settings.STRIPE_SECRET_KEY
        order = get_object_or_404(OrderDetail,stripe_payment_intent=session.id)
        order.has_paid=True
        order.save()
        return render(request,self.template_name)

class PaymentFailedView(TemplateView):
    template_name='myapp/payment_failed.html'