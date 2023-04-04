from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""A form used for user registration, which extends Django's built-in 
    UserCreationForm. In addition to the fields provided by UserCreationForm, 
    this form includes fields for first name and email.
"""

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        '''A class that provides metadata for the RegisterForm class. In this case, 
        it specifies the model to use for the form (User) and the fields to include 
        in the form.
        '''
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        
#from django import forms
#from django.forms import ModelForm
#from . models import Booking

#Create a book form 

#class BookForm(ModelForm):
 #   class Meta:
  #     model = Booking
   #    fields = ('name', 'address', 'postal', 'phone', 'email_address')