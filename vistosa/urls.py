from django.contrib import admin
from django.urls import re_path, path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('apps.dashboard.urls')),
    re_path(r'^accounts/', include('apps.accounts.urls')),
    re_path(r'^dashboard/employee_master/', include('apps.employee_master.urls')),
    re_path(r'^dashboard/attendance_register/', include('apps.attendance_register.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
