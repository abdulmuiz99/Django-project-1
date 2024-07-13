from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to the django course")

    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Who we are, Let us Know")
    return render(request, 'website/aboutus.html')

def services(request):
    # return HttpResponse("What are our services, try it out")
    return render(request, 'website/services.html')

def contact(request):
    # return HttpResponse("Just know us what can we do for you")
    return render(request, 'website/contact.html')