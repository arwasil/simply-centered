from django.shortcuts import render

def index(request):
  return render(request, 'main/index.html')

def board(request, slug):
  context = {
    'name' : " ".join([v.capitalize() for v in slug.split("-")]),
    'slug' : slug
  }

  return render(request, 'main/board.html', context)