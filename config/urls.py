
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('security/', admin.site.urls),
    path('',include('new.urls')),
    path('interaction/',include('intractions.urls')),
    path('i18n/',include('django.conf.urls.i18n')),
    path('accounts/',include('akkounts.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)