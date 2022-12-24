from django.shortcuts import render # To render the signupaccount.html template
from django.contrib.auth.forms import UserCreationForm # This is the form provided by Django to easily create a signup form to register new users
from .forms import UserCreateForm # This is the form we created in forms.py
from django.contrib.auth.models import User # To create a new user
from django.contrib.auth import login # To log the user in after they have successfully created an account
from django.contrib.auth import logout # To log the user out
from django.shortcuts import redirect # To redirect the user to the home page after they have successfully created an account
from django.db import IntegrityError # To handle the error when a user tries to create an account with a username that already exists    

# Create your views here.
def signupaccount(request):
    """
        UserCreationFrom is provide by Django to easily create a signup form
        to register new users.
    """
    if request.method == 'GET': # When the user first visits the page (localhost:8000/accounts/signupaccount), show them a blank form
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else: # When the user submits the form, create a new user
        if request.POST['password1'] == request.POST['password2']: # Check if the two passwords match
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) # Create a new user
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError: # If the user tries to create an account with a username that already exists, show them an error message
                return render(request,
                'signupaccount.html',
                {'form': UserCreateForm,
                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signupaccount.html',
            {'form': UserCreateForm, 'error': 'Passwords do not match'})


def logoutaccount(request):
    logout(request)
    return redirect('home')