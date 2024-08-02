"""
URL configuration for FDP project.

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
from django.urls import path,include
from FDP.views import hello_world

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_world),
    path('',include("module1.urls")),
    path('',include("currdatetime.urls")),
    path("program2/",include("program2.urls")),
    path("program3/",include("program3.urls")),
    path("program4/",include("program4.urls")),
    path("program5/",include("program5.urls")),
    path("program7/",include("program7.urls")),
    path("program8/",include("program8.urls")),
    path("program9/",include("program9.urls")),
    path("program9/",include("program9.urls")),
    path("program10/",include("program10.urls"))
]
