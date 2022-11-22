from email.utils import decode_rfc2231
from django.shortcuts import render

# Create your views here.
def adbook_home(request):
    return render(request,'adbook/home.html')

def adbook_aboutus(request):
    return render(request,'adbook/aboutus.html')

def adbook_author(request):
    return render(request,'adbook/author.html')

def adbook_explore(request):
    return render(request,'adbook/exlpore.html')

def adbook_book(request):
    return render(request,'adbook/book.html')

    
def adbook_login(request):
    return render(request,'adbook/login.html')

    
def adbook_register(request):
    return render(request,'adbook/register.html')