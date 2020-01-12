from django.shortcuts import render
#from appTwo.models import User
#from django.http import HttpResponse
from appTwo.forms import NewUser
# Create your views here.
def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form=NewUser()
    if request.method=="POST":
        form=NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            printn("ERROR: FORM INVALID")

    return render(request,'appTwo/users.html',{'form':form})
