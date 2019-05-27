from django.views import generic
from django.shortcuts import render, render_to_response,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, Catalogue, Bug, Feature, ArtForm
from django.utils import timezone #importing the timezone model
from datetime import datetime, timedelta # import to filter new recipes
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from . forms import UserSignUpForm #custome signup form
from django.contrib.auth.decorators import login_required

#INDEX VIEW
def index(request):
    context={
        'index': 'active'
    }
    return render(request, 'artist/index.html', context)

#START VIEW
def start(request):
    
    context={
        'index': 'active'
    }
    return render(request, 'artist/start.html', context)
    
#CATALOGUE VIEW
@login_required
def catalogue(request):
    qs = Catalogue.objects.all()
    
    context={
        'qs': qs,
        'catalogue': 'active'
    }
    return render(request, 'artist/catalogue.html',context)

#BUG VIEW
@login_required
def bug(request):
    bugs = Bug.objects.all()

    context={
        'bug': 'active'
    }
    return render(request, 'artist/bugs.html', context)
    
#FEATURE VIEW
@login_required
def feature(request):
    features = Feature.objects.all()
    
    context={
        'feature': 'active'
    }
    return render(request, 'artist/features.html', context)

#ABOUT VIEW
def about(request):
    context={
        'about': 'active'
    }
    return render(request, 'artist/about.html', context)
    