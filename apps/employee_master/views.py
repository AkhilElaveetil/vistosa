from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class EmployeesListView(TemplateView):
    template_name = "employee_master/employees_list.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeesListView, self).get_context_data(**kwargs)

        return context
        

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


