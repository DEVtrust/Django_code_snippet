from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('index', views.index, name='index'),
     path("login", views.login, name="login"),
     path('', views.test, name="test"),
     path('cancel/<int:id>', views.cancel, name="cancel"),
     path('show1/', views.show1, name="show1"),  
     path('show2/', views.show2, name="show2"), 
     path("logout", views.logout_request, name="logout"),
     path('delete/<int:id>', views.delete, name="delete"),
     path('deleteall/<int:id>', views.deleteall, name="deleteall"),
     #path('test', views.test, name="test"),
     path('datatable', views.datatable,name='datatable'),

]