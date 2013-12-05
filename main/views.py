from django.shortcuts import render, get_object_or_404

import requests, simplejson as json

from models import *


def index(request):
  menu = Category.objects.filter(parent=None, show_in_menu=True)[0:4]
  return render(request, 'main/index.html', {'menu': menu})

def board(request, *slugs):
  category = get_object_or_404(Category, slug=slugs[-1])

  params = {
    'limit': 6,
    'format': 'json',
    'tags': [category.name]
  }

  url = 'http://7gportal.spling.com/api/2/recommendation/'
  response = requests.get(url, params=params)
  spling_data = response.json()

  return render(request, 'main/board.html', {'category': category, 'data': spling_data['items']})

def spling(request):

  context = {
    'url' : request.GET.get('url')
  }

  return render(request, 'main/spling.html', context)

def shop(request):
  categories = Category.shop_categories.filter(parent=None)

  url = 'http://spling.com/api/2/recommendation/?limit=8&format=json'
  response = requests.get(url)
  spling_data = response.json()

  return render(request, 'main/shop.html', {'categories': categories, 'data': spling_data['items']})