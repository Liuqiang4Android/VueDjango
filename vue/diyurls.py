from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path,re_path
from vue import views

urlpatterns = [

    path('add_book', views.add_book, ),
    path('show_books', views.show_books, ),
]