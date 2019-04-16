from django.shortcuts import render, get_object_or_404
from models import Craft

def index(request):
    #pull all crafts objects
    Crafts =Craft.objects.all()
    context = {'Craft':Craft,}
    return render(request, 'artist/index.html', {'Craft':Craft})
    
#http 404 error
def detail(request, work_id):
    artist = get_object_or_404(Artist, id=work_id)
    return render(request, 'artist/detail.html', {'Craft': Craft})
