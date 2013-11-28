from django.shortcuts import render, get_object_or_404

import requests, simplejson as json

from models import *


def index(request):
  categories = Category.objects.filter(parent=None)
  return render(request, 'main/index.html', {'categories': categories})

def board(request, *slugs):
  category = get_object_or_404(Category, slug=slugs[-1])

  url = 'http://spling.com/api/2/recommendation/?limit=6&format=json'
  response = requests.get(url)
  spling_data = response.json()

  return render(request, 'main/board.html', {'category': category, 'data': spling_data['items']})

def spling(request):

  context = {
    'url' : request.GET.get('url')
  }

  return render(request, 'main/spling.html', context)

def shop(request):
  categories = Category.objects.filter(parent=None)

  url = 'http://spling.com/api/2/recommendation/?limit=8&format=json'
  response = requests.get(url)
  spling_data = response.json()

  return render(request, 'main/shop.html', {'categories': categories, 'data': spling_data['items']})