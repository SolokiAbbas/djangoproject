from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Success")
    return render(request, 'first_app/form_page.html', {'form':form})
