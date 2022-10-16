from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Bantuan.views import web1
from Beranda.views import web2
from Fitur.views import web3
from Tentang.views import web4
from matematika.settings import STATIC_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bantuan', web1),
    path('Beranda', web2),
    path('Fitur', web3),
    path('Tentang', web4),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)