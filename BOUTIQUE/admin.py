from django.contrib import admin
from django.utils.html import format_html
from BOUTIQUE.models import Boutique, Contact, Order
from django.contrib.admin import AdminSite
from .models import Order
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
    list_display = ('title', 'name', 'email', 'phone', 'ordered_at', 'quantity')



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'desc')
    search_fields = ('name', 'email')

admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)

class MyAdminSite(AdminSite):
    site_header = 'My Administration'
    site_title = 'Site Admin'
    index_title = 'Admin Dashboard'

admin_site = MyAdminSite(name='myadmin')