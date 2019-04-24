from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, GroupMember, Catalogue, Bug, Feature

def index(request):
    artist = Artist.Catalogue.filter().order_by('Year')
    return render(request, 'artist/index.html',{})

def start(request):
    return render(request, 'artist/start.html',{})

def catalogue(request):
    return render(request, 'artist/catalogue.html',{})

def login(request):
    return render(request, 'artist/registration/login.html',{})