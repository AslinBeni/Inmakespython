from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
from django.shortcuts import redirect

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
       username = request.POST['username']
       firstname = request.POST['first_name']
       lastname = request.POST['last_name']
       emailid = request.POST['email']
       password = request.POST['password']
       cpassword = request.POST['password1']
       if password==cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,"username taken")
               return redirect('register')
           elif User.objects.filter(email=emailid).exists():
               messages.info(request,"email taken")
               return redirect('register')
           else:
               user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=emailid,password=password)
               user.save()
               return redirect('login')
       else:
           messages.info(request,"password not match")
           return redirect('register')
           return redirect('/')
    return render(request,"register.html")

