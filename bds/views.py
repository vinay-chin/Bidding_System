from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse


def index(request):
    if request.method =='POST':
        messages.success(request, 'bsdk')

    template = loader.get_template('index.html')
    return HttpResponse(template.render()) 

def logreg(request):
    template = loader.get_template('logreg.html')
    return HttpResponse(template.render()) 

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render()) 

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        username = form.cleaned_data.get('username') 
        messages.success(request, 'Your account has been created ! You are now able to log in')
        return redirect('login')
    else:
        template = loader.get_template('signup.html')
        return HttpResponse(template.render())         
from bds.models import form

def form_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phno')
        comment = request.POST.get('message')
        print(name,email,phone,comment)
        fi=form(name=name,email=email,phno=phone,message=comment)
        fi.save()
    return render(request, 'index.html') 
    