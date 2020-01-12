from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("this about")

def contact(request):
    return HttpResponse("this contact")

def tracker(request):
    return HttpResponse("this tracker")

def search(request):
    return HttpResponse("this search")    

def productView(request):
    return HttpResponse("this product view")

def checkout(request):
    return HttpResponse("this about")
