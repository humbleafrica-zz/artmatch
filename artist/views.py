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



#view functions
def index(request):
    context={
        'index': 'active'
    }
    return render(request, 'artist/index.html', context)

def start(request):
    
    context={
        'index': 'active'
    }
    return render(request, 'artist/start.html', context)
    
@login_required
def profile(request):
    #qs = Artist.objects.filter(pk=pk)
    context={
       # 'qs': qs,
        'index': 'active'
    }
    return render(request, 'artist/profile.html', context)

"""def profile(request, pk):
    qs = Artist.objects.filter(pk=pk)
    context={
        'qs': qs,
        'index': 'active'
    }
    return render(request, 'artist/profile.html', context)
"""
@login_required
def catalogue(request):
    qs = Catalogue.objects.all()
    
    context={
        'qs': qs,
        'catalogue': 'active'
    }
    return render(request, 'artist/catalogue.html',context)

@login_required
def bug(request):
    bugs = Bug.objects.all()

    context={
        'bug': 'active'
    }
    return render(request, 'artist/bugs.html', context)

@login_required
def feature(request):
    features = Feature.objects.all()
    
    context={
        'feature': 'active'
    }
    return render(request, 'artist/features.html', context)

def about(request):
    context={
        'about': 'active'
    }
    return render(request, 'artist/about.html', context)
    
def login(request):
    context={
        'about': 'active'
    }
    return render(request, 'artist/catalogue.html', context)

def logout(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_date.get('username')
            messages.success(request, 'Account created for {username}, please login')
            form.save()
        return redirect('login')
    else:
        form = UserSignUpForm()
    context ={
        'form': form,
    }
    return render(request, 'registration/logout.html')
  
  
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_date.get('username')
            messages.success(request, 'Account created for {username}, please login')
            form.save()
        return redirect('login')
    else:
        form = UserSignUpForm()
    context ={
        'form': form,
    }
    return render(request, 'registration/signup.html', context)