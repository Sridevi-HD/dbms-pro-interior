from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def kitchen(request):
    return render(request,"kitchen.html")

def livingroom(request):
    return render(request,"livingroom.html")

def bedroom(request):
    return render(request,"bedroom.html")

def about(request):
    return render(request,"about.html")

def price(request):
    return render(request,"price.html")

def testi(request):
    return render(request,"testi.html")

def regidesigner(request):
    return render(request,"regidesigner.html")

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if  user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html")

def regester(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
    

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('regester')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('regester') 
        return redirect('/') 
    else:
        return render(request,'regester.html')


def logout(request):
    auth.logout(request)
    return redirect('/')        
                 
        
        



