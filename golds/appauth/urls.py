from django.urls import path
from appauth import views

urlpatterns = [
   path('',views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('handlelogin', views.handlelogin, name="handlelogin"),
   path('logout', views.handleLogout, name="handleLogout"),
   path('contact', views.contact, name="contact"),
   path('join', views.enroll, name='join'),
   path('services', views.services, name='services'),
   path('about', views.about, name='about'),
   path('profile', views.profile, name='profile'),
   path('gallery', views.gallery, name='gallery'),
   path('attendance', views.attendance, name='attendance')

   
]
    