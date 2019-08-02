from django.contrib import admin
from django.urls import path
import products.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
