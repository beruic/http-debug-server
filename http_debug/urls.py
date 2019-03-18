from django.conf.urls import url

from http_debug.views import detect

urlpatterns = [
    url(r'^', detect),
]
