from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from BOUTIQUE.models import Boutique, Contact
from .models import Order, Product
import math
import logging, requests
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def boutique(request):
    no_of_posts = 1
    page = int(request.GET.get('page', 1))
    
    boutiques = Boutique.objects.all()
    total_boutiques = boutiques.count()

    boutiques = boutiques[(page - 1) * no_of_posts: page * no_of_posts]

    prev = page - 1 if page > 1 else None
    nxt = page + 1 if page < math.ceil(total_boutiques / no_of_posts) else None

    context = {'boutiques': boutiques, 'prev': prev, 'nxt': nxt}
    return render(request, 'new_arrivals.html', context)


def boutique_post(request, slug):
    """Displays a detailed view of a boutique post."""
    boutique = get_object_or_404(Boutique, slug=slug)
    return render(request, 'boutique_detail.html', {'boutique': boutique})

@login_required
@csrf_exempt
def new_arrivals_view(request):
    """Lists all new arrivals."""
    new_arrivals = Boutique.objects.all()
    return render(request, 'new_arrivals.html', {'new_arrivals': new_arrivals})


def product_detail(request, slug):
    product = get_object_or_404(Boutique, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

@login_required
@csrf_exempt
def order_view(request, product_id=None):
    """Displays the order form with a selected product."""
    selected_product = get_object_or_404(Boutique, sno=product_id) if product_id else None

    context = {
        'selected_product': selected_product,
    }
    return render(request, 'order.html', context)

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        product_sno = request.POST.get('product_sno')  # Get the product sno from form

        # Fetch the product object using the sno field
        product = get_object_or_404(Boutique, sno=product_sno)

        # Create the order object
        Order.objects.create(
            title=product.title,  # Use the product title here
            name=name,
            email=email,
            phone=phone,
            address=address,
            quantity=quantity,
        )

        messages.success(request, 'Order placed successfully!')
        return redirect('order')

    return redirect('order')



@login_required
@csrf_exempt
def search(request):
    """Handles search functionality."""
    query = request.GET.get('q', '')
    results = Boutique.objects.filter(title__icontains=query) if query else Boutique.objects.none()
    return render(request, 'search.html', {'results': results})

@login_required
@csrf_exempt
def contact(request):
    """Handles contact form submissions."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        Contact.objects.create(name=name, email=email, phone=phone, desc=desc)
        messages.success(request, 'Contact submitted successfully!')
        return redirect('contact')

    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')