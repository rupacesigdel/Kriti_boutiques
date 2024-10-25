from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_arrivals/', views.new_arrivals_view, name='new_arrivals'),
    path('boutique_post/<slug:slug>/', views.boutique_post, name='boutique_post'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order/', views.order_view, name='order'),
    path('order/<int:product_id>/', views.order_view, name='order'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]
