from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "variable":"the var is sent"
    }
    return render(request, 'index.html ',context)
    # return HttpResponse("his is ayeeshas home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("his is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("his is services page")
 
def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("his is contact page")
 
