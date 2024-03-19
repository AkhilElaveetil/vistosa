from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from .forms import LoginForm
from .utils import get_sha_hash
from apps.vcd_db.models import Usermaster
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class LoginView(TemplateView):
    template_name = "accounts/index.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        form = LoginForm(self.request.POST or None)
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        context = self.get_context_data(**kwargs)
        form = context["form"]
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['pwd']
            if password:
                ins_user = Usermaster.objects.get(username=username)
                if not ins_user:
                    context['errors'] = "Invalid Username, Please try again"
                else:
                    if ins_user.userpassword == get_sha_hash(password):
                        # Check if the user exists in Django's User model
                        user = User.objects.filter(username=username).first()
                        if user is None:
                            # If user doesn't exist, create a new user
                            user = User.objects.create_user(
                                username=username, password=password, is_superuser=True)

                        # Authenticate user
                        user_auth = authenticate(request, username=username, password=password)
                        if user_auth:
                            for s in Session.objects.all():
                                if s.get_decoded().get('_auth_user_id') == str(user_auth.id):
                                    s.delete()
                            login(request, user)
                            return redirect(reverse_lazy('dashboard:base-dashboard'))
                        else:
                            context['errors'] = "Incorrect password"
                    else:
                        context['errors'] = "Invalid Password, Please try again"
            else:
                context['errors'] = "Password is required"
        return self.render_to_response(context)



