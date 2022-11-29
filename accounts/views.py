from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupaccount(request):
    """
        UserCreationFrom is provide by Django to easily create a signup form
        to register new users.
    """
    return render(request, 'signupaccount.html', {'form': UserCreationForm})

