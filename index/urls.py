from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index-home'),
    path('index', views.home, name='login-home'),
    path('signout', views.logout_view, name='logout')
]