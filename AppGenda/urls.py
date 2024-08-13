from django.urls import path
from AppGenda import views

urlpatterns = [
    path('', views.inicio),
    path('todo/', views.todo),
    path('vence/', views.duedates)
]
