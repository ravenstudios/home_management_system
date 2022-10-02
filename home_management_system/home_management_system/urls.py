from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('hms/', include('hms.urls')),
    path('finances/', include('finances.urls')),
    path('accounts/', include('accounts.urls')),
    path('shopping_list/', include('shopping_list.urls')),
    path('messenger/', include('messenger.urls')),
    path('text_message/', include('text_message.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
