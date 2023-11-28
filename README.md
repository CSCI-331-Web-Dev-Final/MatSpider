# MatSpider
CSCI331 Wed Dev Final - Django Web Mathmatics demo
---------------------
INSTALLATION INSTRUCTIONS:

1: Create project Folder at destination
2: Setup git upstream access
3: Setup python virtual enviroment
    3.1: Django
        run "pip install Django" in terminal
    3.2: Matplotlib
        Run "pip install Matplotlib" in terminal
    3.3: ________   
---------------------
RUNTIME INSTRUCTIONS:
    
1:Starting the Django Server 
    Change to project directory located next to "manage.py" and run 
    "python manage.py runserver 8000>" in terminal
    this starts the development server  
2:Linking to Source code

----------------------

---LOG---
(Forrest)
11/22: Linked venv path to github (GoblinTrees), Expanded README OUTLINE
11/23: Added Django resources and runserver
11/24: Created plotr app file, after running server visit "localhost 8000/MatSpider/"
(Ryan Dreyer)
11/25: created and index html file running on server visit "http://127.0.0.1:8000/" (note dont know why it was so hard to build up) ```"""
URL configuration for final_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from start_site.views import index, response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

```
views.py
```
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
```
index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test site</title>
</head>
<body>
    <h1>Test Site</h1>
    
    <input type="text">
    {% comment %} <img src="{{ url_for('image', filename='plot.png') }}" alt="Matplotlib Plot"> {% endcomment %}
</body>
</html>
```

11/27: got response page loaded on local device. 
url.py
```
"""
URL configuration for final_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from start_site.views import index, response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('response.html/',response, name='response'),
    
]
```
views.py
```
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def response(request):
    return render(request,'response.html')
```
index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test site</title>
</head>
<body>
    <h1>Test Site</h1>
    
    <input type="text">
    <a href ="{% url 'response' %}"><button>Submit</button></a>

    {% comment %} <img src="{{ url_for('image', filename='plot.png') }}" alt="Matplotlib Plot"> {% endcomment %}
</body>
</html>
```

