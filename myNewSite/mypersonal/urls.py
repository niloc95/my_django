from django.urls import path

from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.bookings, name='bookings'),
]
