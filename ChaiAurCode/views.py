from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hellow ! You are at home page!")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("Hellow ! You are at about page!")


def contact(request):
    return HttpResponse("Hellow ! You are at contact page!")
