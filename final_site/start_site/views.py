from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64



# Create your views here.
def index(request):
    return render(request,'index.html')
def response(request):
    return render(request,'response.html')


