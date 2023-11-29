from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot


#getPlot takes in the data from the form data and parses it for symbolic values
#it then
def getPlot(s):
    #note s is string input from the user in index or response html forms
    #it then saves the file to the static file

    func = parse_expr(s)
    p1 = plot(func, show=False)
    #print(type(p1)) #Debugging
    p1.save('plotr/static/images/data.png')
    #p1.show()   #show to the coder for debug - order matters, save first then show (see matplotlib doc)
    #ERR: the above debug is depreciated- better method is plot(func, show=True) above - the above throws errors



#The Form API for Django-used to reduce boilerplate tasks with Forms.
#Note it is still possible to use regular HTML form data simultaniously
class dataForm(forms.Form):
    # each field would be mapped as an input field in HTML
    data = forms.CharField(max_length=200)

# Create your views here. <--- this message is standard when starting new Django project

#landing page with start of the process
def index(request):
    return render(request, 'index.html')


#excempt decorator used to simplify the dev process- normally, it is required to validate the form data
#before the webpage will utilize it - see Django Form API docs
@csrf_exempt
def response(request):
    template = "response.html"

    if request.method == "GET":
        d = request.GET.lists()
        print("---")
        #for loop to display all retrieved data - GET used to show in URL and allow backtracking/copypaste
        #recursive form, so the page loops to itself
        for key, value in request.GET.lists():
            #print("Key: " + str(key))
            #print("Val: "+ str(value))
            global val
            val = str(value)[2:-2]
    con = {"data": val}

    #create the saved files in the png folder
    getPlot(val)
    return render(request, template, con)



#this page is just to show another way to create a page:
#typical use would have the user "write" the html in the function space and return the HttpResponse
def plotr(request):
    html = "<h1>Now you're at the Plotr page</h1>"
    return HttpResponse(html)