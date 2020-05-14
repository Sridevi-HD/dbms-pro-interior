from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from design.models import Bookingdetails


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

def thanks(request):
    return render(request,"thanks.html")    

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
                 
        
def booking(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        user_name = request.POST['user_name']
        phone_no = request.POST['phone_no']
        address1 = request.POST['address1']

        paymode = request.POST['paymode']
        cc_name = request.POST['cc_name'] 
        cc_number = request.POST['cc_number']
        cc_experation = request.POST['cc_expiration']
        cc_cvv = request.POST['cc_cvv'] 

        user1=Bookingdetails.objects.create(first_name=first_name,user_name=user_name,phone_no=phone_no,address1=address1,paymode=paymode,cc_name=cc_name,cc_experation=cc_experation,
        cc_number=cc_number,cc_cvv=cc_cvv)
        user1.save() 
        return redirect('thanks')   
    else:
        return render(request,'booking.html')





        
        



