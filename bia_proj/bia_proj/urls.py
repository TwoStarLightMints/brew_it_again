from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bia.urls')),
    path('calculator/', include('coffee_ratio_calculator.urls')),
]
