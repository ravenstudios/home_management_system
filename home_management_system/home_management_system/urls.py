from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hms/', include('hms.urls')),
    path('finances/', include('finances.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
