from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name="login"),
    path('register', views.register_page, name="register"),
    path('logout', views.logout_page, name="logout"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
