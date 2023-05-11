from django.urls import path
#from .views import home_view
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.bookings, name='bookings'),
    path('home/<str:id>/', views.home, name='home'),
]
