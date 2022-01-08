from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from app.urls import router as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
]
