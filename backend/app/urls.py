from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import static
from django.conf import settings

from .views import redirect_blog

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
