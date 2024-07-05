from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Profile
from django.contrib.auth.models import User


def register(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, "Registration successful.")
            return redirect(reverse_lazy('users:createprofile'))
    else:
        form = NewUserForm()
    
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def logout_view(request):

    logout(request)
    return render(request,'users/logout.html')


@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def create_profile(request):

    if request.method == 'POST':
        contact_number=request.POST.get('contact_number')
        image=request.FILES['upload']
        user=request.user
        if Profile.objects.filter(user=user).exists():
            profile=Profile.objects.get(user=user)
        else:
            profile=Profile(user=user,image=image,contact_number=contact_number)
        profile.save()
        return redirect(reverse_lazy('myapp:products'))
    return render(request,'users/createprofile.html')


def seller_profile(request,id):
    seller=User.objects.get(id=id)
    context={
        'seller':seller
    }
    return render(request,'users/sellerprofile.html',context)