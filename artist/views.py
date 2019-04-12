from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> this is this is the home page</h1>")
    
def detail(request):
   return HttpResponse("<h2>Details for Craft id: "+ str(id) + "</h2>")