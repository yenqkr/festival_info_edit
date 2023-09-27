from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls', namespace='order'),),
    path('', include('mainpage.urls', namespace='mainpage'),),
    path('main/', include('main.urls', namespace='main')),
    path('booth/', include('booth.urls', namespace='booth')),
    path('visitor/', include('visitor.urls', namespace='visitor')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

