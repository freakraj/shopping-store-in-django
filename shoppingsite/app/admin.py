from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product,User


   


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'title', 'selling_price', 'discounted_price',  'description', 'brand', 'category', 'product_image']



 def product_info(self, obj):
  link = reverse("admin:app_product_change", args=[obj.product.pk])
  return format_html('<a href="{}">{}</a>', link, obj.product.title)




