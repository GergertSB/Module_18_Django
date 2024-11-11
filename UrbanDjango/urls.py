"""
URL configuration for UrbanDjango project.

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
from django.urls import path, include
from task2.views import func_templ, Сlas_templ
from task3.views import index, index1, index2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', func_templ),
    path('2/', Сlas_templ.as_view()),
    path('', index),
    path('shop_page/', index1),
    path('cart_page/', index2),
    path('menu/', include('task4.urls')),
    path('registration/', include('task5.urls')),
]
