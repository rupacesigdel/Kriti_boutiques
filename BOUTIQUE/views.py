from django.shortcuts import render, redirect, get_object_or_404
from BOUTIQUE.models import Boutique, Contact
import math
from django.urls import reverse
from .models import Boutique
from django.contrib import messages
from .models import Order  

def home(request):
    return render(request, 'index.html')

def boutique(request):
    no_of_posts = 7
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    boutiques = Boutique.objects.all()
    length = len(boutiques)
    boutiques = boutiques[(page - 1) * no_of_posts: page * no_of_posts]

    prev = page - 1 if page > 1 else None
    nxt = page + 1 if page < math.ceil(length / no_of_posts) else None

    context = {'boutiques': boutiques, 'prev': prev, 'nxt': nxt}
    return render(request, 'home.html', context)

def boutique_post(request, slug):
    boutique = Boutique.objects.filter(slug=slug).first()
    context = {'boutique': boutique}
    return render(request, 'boutique_post.html', context)

def order_view(request):
    if request.method == 'POST':
        return redirect(reverse('home')) 
    return render(request, 'order.html')


def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Retrieve phone number
        address = request.POST.get('address')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')

        Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            product=product,
            quantity=quantity
        )

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order')
    return render(request, 'order.html')


def new_arrivals_view(request):
    new_arrivals = Boutique.objects.all() 
    context = {
        'new_arrivals': new_arrivals
    }
    return render(request, 'new_arrivals.html', context)


def product_detail(request, sno):
    product = get_object_or_404(Boutique, sno=sno)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

    
def search(request):
    query = request.GET.get('q')
    if query:
        results = Boutique.objects.filter(title__icontains=query)
    else:
        results = Boutique.objects.none()

    return render(request, 'search.html', {'results': results})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()
        return redirect('contact')
    return render(request, 'contact.html')
