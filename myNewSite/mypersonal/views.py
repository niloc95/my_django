from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .forms import BookForm
from . forms import RegisterForm

# Create your views here.
def base(request):
    '''
    Renders the base.html template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the rendered base.html template.
    '''
    return render(request,'base.html')

def home(request):
    return render(request,'nilo/home.html')

def about(request):
    return render(request,'nilo/about.html')

def links(request):
    return render(request,'nilo/links.html')

def contact(request):
    return render(request,'nilo/contact.html')

def bookings(request):
    return render(request,'nilo/bookings.html')

def bookings(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, 'nilo/bookings.html', {'form':form})

