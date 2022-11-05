from django.shortcuts import render, redirect
from .models import Appoinment
from django.contrib import messages

# Create your views here.
def home(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        option = request.POST['option']
        date = request.POST['date']
        data = Appoinment.objects.create(name=name, phone=phone, email=email, work=option, date=date)
        data.save()
        messages.success(request, 'Thank You For Contacting! We will get back to yo soon')
        return redirect("/")
    return render(request, 'socm/socmhome.html')

def about(request):
    return render(request, 'socm/socmabout.html')

def contact(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        option = request.POST['option']
        date = request.POST['date']
        data = Appoinment.objects.create(name=name, phone=phone, email=email, work=option, date=date)
        data.save()
        messages.success(request, 'Thank You For Contacting! We will get back to yo soon')
        return redirect("/")
    return render(request, 'socm/socmcontact.html')

def wedding(request):
    return render(request, 'socm/socmwedding.html')

def glamour(request):
    return render(request, 'socm/socmglamour.html')

def hairstyle(request):
    return render(request, 'socm/socmhairstyle.html')

def work(request):
    return render(request, 'socm/socmwork.html')
