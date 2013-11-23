from django.shortcuts import render, get_object_or_404

from models import *

def index(request):
  return render(request, 'main/index.html')

def board(request, *slugs):
  category = get_object_or_404(Category, slug=slugs[-1])
  return render(request, 'main/board.html', {'category': category})

def spling(request):

  context = {
    'url' : request.GET.get('url')
  }

  return render(request, 'main/spling.html', context)

def shop(request):
  return render(request, 'main/shop.html', {})