from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = 'Hello there'
    greeting = 'Welcome to my website'
    return render(request, 'index.html',{'title':title,'greet':greeting})


def about(request):
    return HttpResponse('Hello')


def contact(request):
    return HttpResponse('404')


