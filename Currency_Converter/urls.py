from django.contrib import admin
from django.urls import path,include
from Currency_Converter import views
urlpatterns = [
    #it will direct it to index func of views
    path('',views.index,name = 'home'),
    path('fav',views.fav,name='fav'),
    path('calculator/',views.calculator,name='calculator'),
    path('news/',views.news_feed,name="News")
]
