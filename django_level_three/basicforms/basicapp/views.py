from django.shortcuts import render
from .  import forms
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_view(request):
    form=forms.formName()
    if request.method=='POST':
        form=forms.formName(request.POST)
        if form.is_valid():
            print('validation done')
            print('name: '+ form.cleaned_data['name'])

    return render(request,'basicapp/form_page.html',{'form':form})
