"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from medicalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('main/',views.main),
    #path('feed/',views.feed),
    path('index/',views.index),
    path('feedback/',views.feedback),
    path('infoshow/',views.infoshow),
    path('destroy/<int:id>',views.destroy),
    path('doctorpage/<int:id>',views.doctorpage),
    path('proceed/<int:id>',views.proceed),
    path('pharmacyshow/',views.pharmacyshow),
    path('index1/',views.index1),
    path('index0/',views.index0),
    path('pharmacypage/<int:id>',views.pharmacypage),
    path('prescription/<int:id>',views.prescription),
    path('mail/',views.mail)
]
