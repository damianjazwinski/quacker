from django.urls import path, include
from application import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth.login, {'template_name': 'authentication/login.html'}, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/<slug:username>/', views.profile, name='profile'),
    path('userpanel/', views.userpanel, name='userpanel'),
    path('quack/', views.quack, name='quack'),
    path('follows/', views.follows, name='follows'),
]