from django.contrib import admin
from django.urls import path, include

from .router import router


urlpatterns = [
    path('api/v1/', include((router.urls, 'recipe'), namespace='api-v1')),
    path('admin/', admin.site.urls),
]
