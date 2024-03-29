from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularRedocView.as_view(url_name='schema'),
         name='docs'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger'),
    path('api/v1/videos/', include('videos.urls')),
    path('api/v1/subscription/', include('subscriptions.urls')),
    path('api/v1/chat/', include('chat.urls')),
]
