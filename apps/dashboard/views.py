from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context


class DashboardView(TemplateView):
    template_name = "dashboard/admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        return context

