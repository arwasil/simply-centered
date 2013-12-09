from itertools import chain, repeat

from django.shortcuts import render, get_object_or_404, redirect

from models import *
from api.spling import recommendations


def index(request):
    menu = Category.objects.filter(parent=None, show_in_menu=True)[0:4]
    return render(request, 'main/index.html', {'menu': menu})

def board(request, *slugs):
    category = get_object_or_404(Category, slug=slugs[-1])
    data =  chain(recommendations(category, 'menu'), repeat(None))
    
    return render(request, 'main/board.html', {'category': category, 'data': data})

def spling(request):
    context = {
        'url' : request.GET.get('url')
    }

    return render(request, 'main/spling.html', context)

def market(request, category='market'):
    try:
        category = Category.objects.get(slug=category, show_in_shop=True)
    except Category.DoesNotExist:
        return redirect('shop')

    sub_cats = Category.objects.filter(show_in_shop=True).exclude(slug='market')
    data = recommendations(category, 'market', 8)[:8]

    context = {'category': category, 'categories': sub_cats, 'data': data}
    return render(request, 'main/shop.html', context)
