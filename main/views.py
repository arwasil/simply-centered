from django.shortcuts import render

def index(request):
  return render(request, 'main/index.html')

def board(request, *slugs):
  
  def name(slug):
    # Turn a slug into a name
    return " ".join([v.capitalize() for v in slug.split("-")])

  # How many layers of nesting are there
  max_depth = 2
  # Zero index the section
  section = max(min(len(slugs)-1, max_depth), 0)

  context = {
    'section' : section,
    'names' : map(name, slugs),
    'slugs' : slugs
  }

  return render(request, 'main/board.html', context)