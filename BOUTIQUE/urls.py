from django.urls import path
from BOUTIQUE import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boutique/', views.boutique, name='boutique'),
    path('search/', views.search, name='search'),
    path('boutique_post/<str:slug>/', views.boutique_post, name='boutique_post'),
    path('contact/', views.contact, name='contact'),
]
