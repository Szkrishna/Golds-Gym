from django.urls import path
from appauth import views

urlpatterns = [
   path('',views.Home, name="Home"),
   path('signup', views.signup, name="signup"),
   path('login', views.login, name="login"),
   path('logout', views.logout, name="logout")

   
]
    