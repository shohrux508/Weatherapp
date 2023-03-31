from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.

# a


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class Homeview(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class Authorizedview(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {'today': datetime.today()}


class Nothingview(TemplateView):
    template_name = 'home/just.html'
    extra_context = {'today': datetime.today()}


# same to a
# def welcome(request):
#   return render(request, 'home/welcome.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
