from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormSignUp

# Create your views here.
def SignUp(request):
    return render(request, 'SignUp.html')
    
def index(request):
    return render(request, 'index.html')
    
def singleProduct(request):
    return render(request, 'singleProduct.html')
    
def shop(request):
    return render(request, 'shop.html')
    
def checkout(request):
    return render(request, 'checkout.html')
    
def cart(request):
    return render(request, 'cart.html')
    
def contact(request):
    return render(request, 'contact.html')