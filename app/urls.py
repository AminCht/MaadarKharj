from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView, logout_then_login

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", views.logout, name="logout"),
    path('', views.dashboard),
    re_path(r'^.*\.*', views.pages, name='pages'),
]