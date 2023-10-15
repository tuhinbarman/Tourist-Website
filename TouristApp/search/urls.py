from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.search,name='search'),
    path('results',views.results,name='results'),
    path('results/<int:id>',views.details,name='details')
]