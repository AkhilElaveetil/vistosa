from django.urls import path, re_path
from apps.employee_master import views

app_name = 'employee_master'

handler404 = 'employee_master.views.custom_404_view'
urlpatterns = [
    re_path(r'^$', views.EmployeesListView.as_view(), name='list'),
]