from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Order
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "Hey Guys just smile and be chill your are at Raksha Pizza House")
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def connect(request):
    return render(request, 'connect.html')
    #return HttpResponse("this is services page")

def order(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        order=Order(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        order.save()
        messages.success(request, "Thank you! Your order has been placed.")
    return render(request, 'order.html')
    #return HttpResponse("this is order page")

