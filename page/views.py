from django.shortcuts import render

def home(request):
    return render(request,'page/home.html')

def about(request):
    return render(request,'page/about.html')

def contact(request):
    return render(request,'page/contact.html')
