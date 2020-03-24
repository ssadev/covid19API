from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('bycountry', views.ByCountry, name="ByCountry"),
    path('globaldata', views.globalData, name="globalData"),


]