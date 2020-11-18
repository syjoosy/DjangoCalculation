from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Views.to_home),
    path('home/', views.Views.home, name='home'),
    path('id/', views.Views.ResultRecieve, name='id')
]
