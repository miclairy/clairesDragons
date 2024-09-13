from django.urls import path
from clairesDragonApp import views

urlpatterns = [
    path('', views.index, name='index'),
]