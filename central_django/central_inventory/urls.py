from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('central/', views.index, name="central"),
    path('sites/', views.get_sites)
]