from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, logout_then_login

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", views.logout, name="logout"),
    path('dashboard/', views.dashboard)
]