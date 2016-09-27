from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.cache import never_cache

from django.views.generic import TemplateView
from django.views.generic import FormView

from two_factor.views import OTPRequiredMixin


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class RegistrationFormView(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('registration_complete')

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)


class RegistrationCompleteTemplateView(TemplateView):
    template_name = 'registration_complete.html'

    def get_context_data(self, **kwargs):
        context = super(
            RegistrationCompleteTemplateView, self).get_context_data(**kwargs)
        context['login_url'] = settings.LOGIN_URL
        return context


class TFASecretTemplateView(OTPRequiredMixin, TemplateView):
    '''a page that can only be accessed if TFA was activated for the account.'''

    template_name = 'secret.html'

    @never_cache
    def dispatch(self, request, *args, **kwargs):
        return super(
            TFASecretTemplateView, self).dispatch(request, *args, **kwargs)
