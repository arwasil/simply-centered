from django.shortcuts import render

def index(request):
  return render(request, 'main/index.html')

def board(request, slug):
  context = {
    'name' : " ".join([v.capitalize() for v in name.split("-")]),
    'slug' : name
  }

  return render(request, 'main/board.html', context)