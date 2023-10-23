from django.urls import path
from . import views

# creating url patterns here
urlpatterns = [
    path('', views.welcome),
    path('about/', views.about),
    path('about/contact-us/', views.contact),
]