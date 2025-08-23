from django.contrib import admin
from django.urls import path, include
from usuario.views import home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'), #Raiz do site
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('pedido/', include('pedido.urls')),
    #path('produto/', include('produto.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)