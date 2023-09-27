from django.urls import path
from .views import boothinfo
from django.conf.urls.static import static
from django.conf import settings

app_name = 'booth'

urlpatterns = [
    path('', boothinfo, name='boothinfo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)