from django.shortcuts import render, redirect
from BOUTIQUE.models import Boutique, Contact
import math

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


def search(request):
    return render(request, 'search.html')

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
