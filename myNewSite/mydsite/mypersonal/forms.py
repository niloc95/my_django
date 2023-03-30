from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
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