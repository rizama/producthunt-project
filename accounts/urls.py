from django.urls import path, include
from . import views

urlpatterns = [
        path('signup', views.signup, name='signup'),
        path('signin', views.signin, name='signin'),
        path('logout', views.signin, name='signin'),
    ]
