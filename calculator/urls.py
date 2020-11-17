from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.to_home),
    path('home/', views.home, name='home'),
    path('id/', views.ResultRecieve, name='id')
]
