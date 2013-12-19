from itertools import chain, repeat

from django.shortcuts import render, get_object_or_404, redirect

from models import *
from api import spling as spling_api


def index(request):
    menu = Category.objects.filter(parent=None, show_in_menu=True).order_by('pk')[0:4]

    context = {'menu': menu}
    return render(request, 'main/index.html', context)

def board(request, *slugs):
    category = get_object_or_404(Category, slug=slugs[-1])
    data =  chain(spling_api.recommendations(category, 'menu'), repeat(None))
    
    context = {'category': category, 'data': data}
    return render(request, 'main/board.html', context)

def spling(request):
    context = {'url' : request.GET.get('url')}
    return render(request, 'main/spling.html', context)

def market(request, category='market'):
    try:
        category = Category.objects.get(slug=category, show_in_shop=True)
    except Category.DoesNotExist:
        return redirect('shop')

    sub_cats = Category.objects.filter(show_in_shop=True).exclude(slug='market')
    data = spling_api.recommendations(category, 'market', 8)[:8]

    context = {'category': category, 'categories': sub_cats, 'data': data}
    return render(request, 'main/shop.html', context)

def search(request):
    query = request.POST.get('query', '')
    data =  spling_api.search(query)

    context = {'data': data}
    return render(request, 'main/search.html', context)
