from django.shortcuts import render, get_object_or_404
from models import Craft, Work

def index(request):
    #pull all crafts objects
    Crafts = Craft.objects.all()
    context = {'Craft': Craft,}
    return render(request, 'artist/index.html', {'Crafts':Crafts})
    
#http 404 error
def detail(request, craftid):
    craft = get_object_or_404(Craft, pk=craftid)
    return render(request, 'artist/detail.html', {'craft': craft})

def favorite(request, craftid):
    craft = get_object_or_404(Craft, pk=craftid)
    select_work.is_favorite =True
    select_work.save()
    return render(request, 'artist/detail.html', {'craft': craft})
    
def bugs(request):
    return render(request, 'artist/bugs.html')
    
def features(request):
    return render(request, 'artist/features.html')