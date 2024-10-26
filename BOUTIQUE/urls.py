from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
