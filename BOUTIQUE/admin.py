from django.contrib import admin
from BOUTIQUE.models import Boutique, Contact
from django.contrib.admin import AdminSite

class BoutiqueAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/main.css",)
        }

        js = ("js/blog.js",)


class MyAdminSite(AdminSite):
    site_header = 'My Administration'
    site_title = 'Site Admin'
    index_title = 'Admin Dashboard'

admin_site = MyAdminSite(name='myadmin')


admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Contact)