from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.
#PAssword: Ayushi
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)
        if user is not None:
            return redirect("/")
        else:
            return render(request,'login.html')
    
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login')