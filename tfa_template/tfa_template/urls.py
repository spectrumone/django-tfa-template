"""tfa_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

from .views import HomeTemplateView
from .views import RegistrationFormView
from .views import RegistrationCompleteTemplateView
from .views import TFASecretTemplateView


urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^account/logout/$', auth_views.logout, name='logout'),

    url(r'^account/register/$',
        RegistrationFormView.as_view(),
        name='registration'),

    url(r'^account/register/done/$',
        RegistrationCompleteTemplateView.as_view(),
        name='registration_complete'),

    # a page that can only be accessed if TFA was done logging in.
    url(r'^secret/$',
        TFASecretTemplateView.as_view(),
        name='secret'),

    url(r'^admin/', admin.site.urls),
    url(r'', include(tf_urls + tf_twilio_urls, 'two_factor')),
]
