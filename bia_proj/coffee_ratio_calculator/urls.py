from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.calculator, name="calculator"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
