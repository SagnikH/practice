from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm

from django.contrib import messages
# Create your views here.

def registerUser(request) :

    form = RegisterForm()
    context = {'form':form}

    if request.method == 'POST' :

        form = RegisterForm(request.POST) 

        if form.is_valid():
            form.save()
            messages.success(request, 'User Created succesfully')
            print('user Created')
            return redirect('users:login')
        else :
            print('Not valid')

    return render (request, 'register.html', context)


def loginUser(request) :

    if request.method == "POST" :

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user :
            loginUser(request)
            return redirect('/')

        else :
            messages.info(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')

