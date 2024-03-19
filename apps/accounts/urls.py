from django.urls import re_path
from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^$', views.LoginView.as_view(), name='login'),
]