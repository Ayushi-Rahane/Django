from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime    #This is used to get the current date and time
from django.contrib import messages   #This is used to show the messages on the website

# Create your views here.
def index(request):
 #return HttpResponse("This is Homepage")

 #Variable receiving and sending
 #context is used to send the data to the html file
 context = { 
    'variable1':'This is send 1',
    'variable2':'This is send 2'
 }
 return render(request,'index.html',context)    #render is used to render the html file 

def about_page(request):
 return render(request,'about.html')
 
def services(request):
 return render(request,'services.html')
 
def contact(request):
 if request.method == "POST":
  name = request.POST.get('name')
  email = request.POST.get('email')
  phone = request.POST.get('phone')
  desc = request.POST.get('desc')
  contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
  contact.save()
  messages.success(request, "Your response has been submitted successfully..") #This is used to show the message on the website
  #This is used to save the data in the database

 return render(request,'contact.html')
 
