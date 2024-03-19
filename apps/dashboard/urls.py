from django.urls import path, re_path
from apps.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home-page'),
    re_path(r'^base$', views.DashboardView.as_view(), name='base-dashboard'),
]

