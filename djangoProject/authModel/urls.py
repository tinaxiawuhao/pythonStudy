from django.urls import path
from authModel import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('order/', views.logout),
    path('s_login/', views.s_login),
    path('s_index/', views.s_index),
    path('s_logout/', views.s_logout),
]