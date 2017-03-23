"""MultipleAppsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^courses/', include('apps.courses.urls', namespace='courses')),
    url(r'^login_reg/',include('apps.login_reg.urls', namespace='login_reg')),
    url(r'^random_word/',include('apps.random_word_generator.urls', namespace='random_word')),
    url(r'^survey/',include('apps.survey.urls',namespace='survey')),
    url(r'^timedisplay/',include('apps.timedisplay.urls',namespace='timed'))
]
