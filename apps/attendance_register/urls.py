from django.urls import path, re_path
from apps.attendance_register import views

app_name = 'attendance_register'

handler404 = 'attendance_register.views.custom_404_view'
urlpatterns = [
    re_path(r'^$', views.EmployeeLogListView.as_view(), name='list'),
]