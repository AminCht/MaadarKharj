from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LogoutView, logout_then_login
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path("logout/", views.logout, name='logout'),
    path('', views.dashboard),
    path('me/', views.me, name='me'),
    #path('form/', views.auto, name='form'),
    path(r'^.*\.*', views.pages, name='pages'),
    path('accounts/', include('allauth.urls'))
]