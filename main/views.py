from django.shortcuts import render

def index(request):
  return render(request, 'main/index.html')

def board(request, *slugs):
  
  def name(slug):
    # Turn a slug into a name
    return " ".join([v.capitalize() for v in slug.split("-")])

  context = {
    'names' : map(name, slugs),
    'slugs' : slugs
  }

  return render(request, 'main/board.html', context)