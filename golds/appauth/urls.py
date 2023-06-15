from django.urls import path
from appauth import views

urlpatterns = [
   path('',views.Home, name="Home"),
   path('signup', views.signup, name="signup"),
   path('handlelogin', views.handlelogin, name="handlelogin"),
   path('logout', views.handleLogout, name="handleLogout"),
   path('contact', views.contact, name="contact")

   
]
    