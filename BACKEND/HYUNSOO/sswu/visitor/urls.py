from django.urls import path
from .views import visitor,visitor_write,visitor_more
from visitor.views import visitor_json

app_name = 'visitor'

urlpatterns = [
    path('', visitor, name='visitor'),
    path('write/', visitor_write, name='visitor_write'),
    path('more/', visitor_more, name='visitor_more'),
    path('visitor_json', visitor_json, name='visitor_json')
]