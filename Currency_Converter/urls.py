from django.contrib import admin
from django.urls import path,include
from Currency_Converter import views
urlpatterns = [
    #it will direct it to index func of views
    path('',views.index,name = 'home'),#home page
    path('news/',views.news,name = 'news'),#news page
    path('home/',views.index,name = 'home'),#home page
]
