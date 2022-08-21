from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('', views.index, name='index'),
]
