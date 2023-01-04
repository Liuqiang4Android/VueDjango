from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path,include
from vueProj import views

urlpatterns = [

    path(r'add_book$', views.add_book, ),
    path(r'show_books$', views.show_books, ),
]