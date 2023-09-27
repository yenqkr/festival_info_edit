from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
    path('goods_list/', views.goods_list, name='goods_list'),
    path('reserve/', views.reserve_goods, name='reserve'),
    path('home/', views.home, name='home'),
]
