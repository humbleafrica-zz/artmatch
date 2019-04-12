from django.shortcuts import render
from django.http import HttpResponse
from models import Crafts

def index(request):
    all_crafts =Crafts.objects.all()
    html=''
    for craft in all_crafts:
        url='/craft/'+ str(craft.id)+ '/'
        html+='<a href="'+url+'">craft.work_title</a><br/>'
    return HttpResponse(html)
    
def detail(request):
   return HttpResponse("<h2>Details for Craft ID: "+ str(id) + "</h2>")