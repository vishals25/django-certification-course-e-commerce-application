from django.contrib import admin
from .models import Product,OrderDetail
# Register your models here.

admin.site.site_header='Buy and Sell WebSite'
admin.site.site_title="Site Admin"
admin.site.index_title="Managing The Website,Welcome Admin!"

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','seller')
    search_fields=('name',)
    
    def set_price_discount(self,request,queryset):
        for obj in queryset:
            obj.price = obj.price * 0.9
            obj.save()

    actions=('set_price_discount',)

    list_editable=('price',)

admin.site.register(Product,ProductAdmin)
admin.site.register(OrderDetail)