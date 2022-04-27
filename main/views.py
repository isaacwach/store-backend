from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Booking,Transport
# from .forms import 
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def new_book(request):
    message = 'book it now'
    return redirect(request,'booking.html',{'message':message})
def transport(request):
    message = 'transport'
    return redirect(request,'transport.html',{'message':message})
