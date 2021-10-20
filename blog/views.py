from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import RegisterForm
from .models import Author

# Create your views here.

def create(request):
    form = RegisterForm(request.POST or None)
    message = "Создать человека"
    if request.method == 'POST' and form.is_valid():
        message = "Ok"
        form.save()
        return render(request,"index.html", {"form":form,"message":message})
    return render(request,"index.html", {"form":form,"message":message})

    
def create1(request):
    author =  Author.objects.all()
    message = "All author"
    
    return render(request, 'all.html', {'message':message, 'author': author})

