from django.urls import path
from appauth import views

urlpatterns = [
   path('',views.Home, name="Home")


   
]
    