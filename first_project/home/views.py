from django.shortcuts import render, HttpResponse

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
 return render(request,'contact.html')
 
