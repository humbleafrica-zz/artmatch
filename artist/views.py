from django.http import Http404
from django.shortcuts import render
from models import Craft

def index(request):
    #pull all crafts objects
    Crafts =Craft.objects.all()
    context = {'Craft':Craft,}
    return render(request, 'artist/index.html', {'Craft':Craft})
    
#http 404 error
def detail(request, work_id):
    try:
        work = Craft.objects.get(id=work_id)
    except Craft.DoesNotExist:
        raise Http404("Craft does not Exist")
    return render(request, 'artist/detail.html', {'Craft': Craft})
