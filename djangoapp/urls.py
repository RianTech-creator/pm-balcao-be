from django.contrib import admin
from django.urls import path, include
from usuario.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'), #Raiz do site
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuario.urls')),
    path('pedido/', include('pedido.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)