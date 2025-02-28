from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.
#PAssword: Ayushi
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def user_login(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login')