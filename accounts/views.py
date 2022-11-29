from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
def signupaccount(request):
    """
        UserCreationFrom is provide by Django to easily create a signup form
        to register new users.
    """
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')

