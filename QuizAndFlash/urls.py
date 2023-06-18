from django.contrib import admin
from django.urls import path, include
from Flash import views as Flash_View
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Flash_View.home,name="Home"),
    path('flash-word/', Flash_View.flash_word, name='flash_word'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
