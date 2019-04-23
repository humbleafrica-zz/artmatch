from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, GroupMember, Catalogue, Bug, Feature

def index(request):
    return render(request, 'artist/index.html',{})

