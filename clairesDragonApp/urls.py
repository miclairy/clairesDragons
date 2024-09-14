from django.urls import path
from clairesDragonApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]
urlpatterns += staticfiles_urlpatterns()