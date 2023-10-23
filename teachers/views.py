from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Emobilis')

def about(request):
    return HttpResponse('About Emobilis')

def contact(request):
    return HttpResponse('Contact us')