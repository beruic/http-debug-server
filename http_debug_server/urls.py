from django.conf.urls import url, include
from django.contrib import admin

from http_debug.views import detect

urlpatterns = [
    url(r'^', detect),
]
