from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    re_path(r'^register/$', views.SignUpView.as_view(), name='register'),
    re_path(r'^signin/$', views.SignInView.as_view(), name='signin'),
    re_path(r'^login/$', views.SignInView.as_view(), name='login'),
    re_path(r'^signout/$', views.SignOutView.as_view(), name='signout'),
    re_path(r'^logout/$', views.SignOutView.as_view(), name='logout'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.Activate.as_view(), name = 'activation'),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(title = _('Password Reset'), html_email_template_name = 'registration/password_reset_email.html'), name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(title = _('Password Reset Done')), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(title = _('Password Reset Confirmation')), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(title = _('Password Reset Complete')), name='password_reset_complete'),
]
