import re
from urllib import request
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        cont = Contact(name=name, email=email, message=message)
        cont.save()
        messages.success(request, "your message has been sent")
    
    return render(request, "contact.html")

def pg1(request):
    return render(request, 'pg1.html')
