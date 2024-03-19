from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class EmployeeLogListView(TemplateView):
    template_name = "attendance_register/attendance_register.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeLogListView, self).get_context_data(**kwargs)

        return context


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


