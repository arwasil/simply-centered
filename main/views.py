from django.shortcuts import render

def index(request):
  return render(request, 'main/index.html')

def board(request, name):
  context = {
    'name' : name
  }

  return render(request, 'main/board.html', context)