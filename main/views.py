from django.shortcuts import render, get_object_or_404

from models import *
from api.spling import recommendations


def index(request):
    menu = Category.objects.filter(parent=None, show_in_menu=True)[0:4]
    return render(request, 'main/index.html', {'menu': menu})

def board(request, *slugs):
    category = get_object_or_404(Category, slug=slugs[-1])
    data = recommendations(category.name)
    
    return render(request, 'main/board.html', {'category': category, 'data': data})

def spling(request):
    context = {
        'url' : request.GET.get('url')
    }

    return render(request, 'main/spling.html', context)

def shop(request, category=None):
    if category:
        category = get_object_or_404(Category, slug=category, show_in_shop=True)
    print category

    sub_cats = Category.objects.filter(parent=category, show_in_shop=True)
    data = recommendations(category)

    return render(request, 'main/shop.html', {'category': category, 'categories': sub_cats, 'data': data})

def video(request, category=None):
    if category:
        category = get_object_or_404(Category, slug=category, show_in_video=True)

    sub_cats = Category.objects.filter(parent=category, show_in_video=True)
    data = recommendations(category)

    return render(request, 'main/shop.html', {'category': category, 'categories': sub_cats, 'data': data})