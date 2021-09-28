from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

#DEBUG esta en true, importamos static, trabajamos en modo desarrollo
#para mostrar las imagenes de las recetas en el navegador

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                   #static('/media/','http://localhost/media/')

