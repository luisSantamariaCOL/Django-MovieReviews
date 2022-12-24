from django.contrib.auth.forms import UserCreationForm # This is the form provided by Django to easily create a signup form to register new users

class UserCreateForm(UserCreationForm): # This is the new form we created in forms.py
    def __init__(self, *args, **kwargs): # This is a special method that is called when a new instance of the form is created
        super(UserCreateForm, self).__init__(*args, **kwargs) # This calls the __init__ method of the parent class (UserCreationForm)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None # Remove the help text (the little question mark) next to the username and password fields
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'}) # Add the class 'form-control' to the username and password fields