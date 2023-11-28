(Ryan Dreyer)
11/25: created and index html file running on server visit "http://127.0.0.1:8000/" (note dont know why it was so hard to build up)
11:27: pushing to Git
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

(Ryan Dreyer)11/27: got response page loaded on local device. 
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
    <form action="{% url 'response' %}" method="post">
        {% csrf_token %}
        <label for="input_data">Enter Data:</label>
        <input type="text" id="input_data" name="input_data" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
