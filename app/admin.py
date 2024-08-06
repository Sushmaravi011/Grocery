from django.contrib import admin
from .models import Product,Customer,Cart

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category', 'display_product_image']

    def display_product_image(self, obj):
        if obj.product_image:
            return('<img src="{}" style="width: 100px; height: 100px;" />', obj.product_image.url)
        return 'No Image'
    
    display_product_image.short_description = 'Product Image'

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']