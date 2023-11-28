from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt


class dataForm(forms.Form):
    # each field would be mapped as an input field in HTML
    data = forms.CharField(max_length=200)

# Create your views here.



@csrf_exempt
def response(request):
    template = "response.html"

    if request.method == "GET":
        d = request.GET.lists()
        print("---")
        for key, value in request.GET.lists():
            print("Key: " + str(key))
            print("Val: "+ str(value))
            global val
            val = str(value)


    con = {"data": val}
    return render(request, template, con)

def index(request):
    return render(request, 'index.html')

def plotr(request):
    return HttpResponse("Now you're at the Plotr page")