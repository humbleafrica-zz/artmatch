from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Crafts

def index(request):
    #pull all crafts objects
    all_crafts =Crafts.objects.all()
    template = loader.get_template('artist/index.html')
    context = {
        'all_crafts':all_crafts,
    }
    
    return HttpResponse(template.render(context,request))
    
def detail(request):
   return HttpResponse("<h2>Details for Craft ID: "+ str(id) + "</h2>")