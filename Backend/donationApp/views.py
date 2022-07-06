from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def blog(request):
    return render(request, 'blog.html')


def cause(request):
    return render(request, 'cause.html')

def contact(request):
    return render(request, 'contact.html')

def single_blog(request):
    return render(request, 'single_blog.html')

def elements(request):
    return render(request, 'elements.html')

def cause_details(request):
    return render(request, 'cause_details.html')

def donate(request):
    return render(request, 'donate.html')

