from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError    

# Create your views here.
def signupaccount(request):
    """
        UserCreationFrom is provide by Django to easily create a signup form
        to register new users.
    """
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request,
                'signupaccount.html',
                {'form': UserCreateForm,
                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signupaccount.html',
            {'form': UserCreateForm, 'error': 'Passwords do not match'})

