from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from home.models import Student
# Create your views here.

def index(request):
    return render(request,'index.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        marks = request.POST.get('marks')
        student = Student(name=name,roll_no=roll_no,marks=marks)
        student.save()
        return redirect('home')
    return render(request,'add_student.html')

def user_login(request):
    return render(request,'login.html')
