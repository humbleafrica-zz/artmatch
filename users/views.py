from django.shortcuts import render
from django.contrib import messages
from artist.forms import UserSignUpForm #custome signup form
from django.shortcuts import render, render_to_response,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

#SIGNUP VIEW
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
    return render(request, 'users/signup.html', context)

#LOGIN VIEW
'''def login(request):
    context={
        'about': 'active'
    }
    return render(request, 'users/login.html', context)
'''
#lOGOUT VIEW
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
    return render(request, 'users/logout.html')
  
#PROFILE VIEW
@login_required
def profile(request):
    #qs = Artist.objects.filter(pk=pk)
    context={
       # 'qs': qs,
        'index': 'active'
    }
    return render(request, 'users/profile.html', context)
