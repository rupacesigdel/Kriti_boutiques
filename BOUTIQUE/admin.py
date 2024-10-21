from django.contrib import admin
from BOUTIQUE.models import Boutique, Contact
from django.contrib.admin import AdminSite
from .models import Order

class BoutiqueAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/main.css",)
        }

        js = ("js/blog.js",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('sno', 'name', 'email', 'phone', 'product', 'quantity', 'order_date')
    search_fields = ('name', 'email', 'product')

admin.site.register(Order, OrderAdmin)



class MyAdminSite(AdminSite):
    site_header = 'My Administration'
    site_title = 'Site Admin'
    index_title = 'Admin Dashboard'

admin_site = MyAdminSite(name='myadmin')


admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Contact)