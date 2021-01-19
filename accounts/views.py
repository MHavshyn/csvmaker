from accounts.forms import AccountCreateForm
from accounts.models import User

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect  # noqa
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


class AccountCreateView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        result = super().form_valid(form)
        request = self.request
        messages.success(request, 'Account successfully created!')

        return result


class AccountLoginView(LoginView):
    template_name = 'login.html'

    def get_redirect_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse('core:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        request = self.request
        messages.success(request, f'{request.user}, hello to LMS!')
        return result


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'

    def get_template_names(self):
        result = super().get_template_names()
        request = self.request
        messages.info(request, 'Goodbye!')
        return result
