#this is my vieuws.py file
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'test.htm',{})

def about(request):
    return render(request,'about.html',{})