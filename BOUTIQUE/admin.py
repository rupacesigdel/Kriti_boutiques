from django.contrib import admin
from django.utils.html import format_html
from BOUTIQUE.models import Boutique, Contact, Order
from django.contrib.admin import AdminSite
from .models import Order, Product
from django.utils.safestring import mark_safe


class BoutiqueAdmin(admin.ModelAdmin):
    list_display = ('sno', 'title', 'short_desc', 'price', 'slug', 'time', 'image_preview')
    search_fields = ('title', 'short_desc')
    prepopulated_fields = {'slug': ('title',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />')
        return "No Image"

    image_preview.short_description = 'Image Preview'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('sno', 'name', 'email', 'phone', 'product', 'quantity', 'order_date')
    search_fields = ('name', 'email', 'product')
    list_filter = ('order_date',)
    ordering = ('-order_date',)

    def product_image(self, obj):
        if obj.product.image:
            return mark_safe(f'<img src="{obj.product.image.url}" style="width: 50px; height: auto;" />')
        return "No Image"

    product_image.short_description = 'Product Image'

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'time')
    search_fields = ('name', 'email')

admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)

class MyAdminSite(AdminSite):
    site_header = 'My Administration'
    site_title = 'Site Admin'
    index_title = 'Admin Dashboard'

admin_site = MyAdminSite(name='myadmin')
