from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('',views.index,name="home"),
    # path('products/',views.products,name='products'),
    # path('products/<int:id>/',views.product_detail,name='product_detail'),
    # path('products/add/',views.add_product,name="add_product"),
    # path('products/update/<int:id>/',views.update_product,name="update_product"),
    # path('products/delete/<int:id>/',views.delete_product,name="delete_product"),

    path('products/',views.ProductListView.as_view(),name='products'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('products/add/',views.ProductCreateView.as_view(),name="add_product"),
    path('products/update/<int:pk>/',views.ProductUpdateView.as_view(),name="update_product"),

    path('products/delete/<int:pk>/',views.ProductDelete.as_view(),name="delete_product"),

    path('products/mylistings/',views.my_listings,name='mylistings'),

### payment:

    path('success/',views.PaymentSuccessView.as_view(),name='success'),
    path('failed/',views.PaymentFailedView.as_view(),name='failed'),
    path('api/checkout-session/<int:id>',views.create_checkout_session,name='api_checkout_session'),
    
]