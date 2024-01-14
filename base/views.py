from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import csv , json
from .models import restaurant 

def homepage(request):
    return HttpResponse("Hello")
