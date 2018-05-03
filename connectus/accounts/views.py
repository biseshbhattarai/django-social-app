from django.shortcuts import render,redirect
from .forms import  RegisterForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Friends
from posts.models import Post
from django.contrib.auth.decorators import login_required

import requests
from bs4 import BeautifulSoup

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

           
            return redirect('login')
           
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
            
@login_required
def profile(request):
   # profile_objects = Profile.objects.all()
    posts = Post.objects.all()
   
    users = User.objects.exclude(id=request.user.id)
    friend = Friends.objects.get(current_user=request.user)
    friends = friend.user.all()
    context = {
        'users':users,
        'friends':friends,
        'posts':posts,
        

    }
    return render(request, 'accounts/profile.html', context)


def change_friends(request, operation, pk):
     friend = User.objects.get(pk=pk)
     if operation == 'add':
        Friends.make_friend(request.user, friend)
     elif operation == 'remove':
        Friends.lose_friend(request.user, friend)
     return redirect('profile')
profile

def view_profile(request, pk=None):
    
    if pk:
        profile = User.objects.get(pk=pk)
    else:
        profile = request.user
    args = {'profile': profile}
    return render(request, 'accounts/home.html', args)


def update_profile(request):
    
    profile  = User.objects.filter(id=request.user.id)
   
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update-profile')
    else:
        form = ProfileForm()
    args = {'profile':profile, 'form':form}
    return render(request, 'accounts/hello.html', args)

def starter(request):
    return render(request, 'accounts/starter.html')




