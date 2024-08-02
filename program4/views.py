from django.shortcuts import render

def layout(request):
    return render(request,'program4/layout.html')

def home(request):
    return render(request,'program4/home.html')

def about(request):
    return render(request,'program4/about.html')

def contact(request):
    return render(request,'program4/contact.html')
    

# Create your views here.
