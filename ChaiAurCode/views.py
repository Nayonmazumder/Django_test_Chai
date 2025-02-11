from django.http import HttpResponse


def home(request):
    return HttpResponse("Hellow ! You are at home page!")


def about(request):
    return HttpResponse("Hellow ! You are at about page!")


def contact(request):
    return HttpResponse("Hellow ! You are at contact page!")
