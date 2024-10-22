from django.urls import path
from BOUTIQUE import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boutique/', views.boutique, name='boutique'),
    path('search/', views.search, name='search'),
    path('boutique_post/<str:slug>/', views.boutique_post, name='boutique_post'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order_view, name='order'),
    path('new_arrivals/', views.new_arrivals_view, name='new_arrivals'),
    path('product_detail/<int:sno>/', views.product_detail, name='product_detail'),
    path('submit_order/', views.submit_order, name='submit_order'),
]
