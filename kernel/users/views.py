from django.utils import timezone
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout

from django.views.generic import CreateView
from django.views.generic import RedirectView
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic import UpdateView

from .forms import SignInForm
from .forms import SignUpForm

from .models import User
from users.models import GeneralProfile
from users.forms import PassengerProfileForm
from users.forms import GeneralProfileForm
from users.forms import UserBasicForm
from users.forms import TransmitProfileForm
from users.forms import DriverProfileForm
from users.forms import DriverBankProfileForm
from users.forms import DriverMachineProfileForm

from painless.tokens import account_activation_token

class SignUpView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = SignUpForm
    template_name = 'registration/authentication.html'
    title = _('Register')


    def form_valid(self, form):
        user = form.save(commit = False)

        user.is_active = False
        user.personality = 1
        user.save()

        subject = _('email verification')
        sender = 'animateidea@gmail.com'
        message = _('link activation has been sent.')
        to_mail = form.cleaned_data['email']
        
        context = {
            "text": message,
            "domain": get_current_site(self.request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            "token": account_activation_token.make_token(user),
        }
        
        html_content = render_to_string('mail/activation.html', context)
        
        try:
            send_mail(subject, message, sender, [to_mail], fail_silently=False, html_message=html_content)
        except BadHeaderError:
            messages.warning(self.request, _('Verification mail doesn\'t sent'))

        messages.success(self.request, _('An email has been sent. Please check your email and click on verification link.'))
        return redirect('signin')

class SignOutView(RedirectView):
    url = reverse_lazy("signin")

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)

class SignInView(FormView):
    success_url = reverse_lazy('signin')
    form_class = SignInForm
    template_name = 'registration/authentication.html'
    title = _('Login')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('samaro:home')
        else:
            messages.warning(self.request, _('username or password is wrong.'))
            return redirect('signin')

class Activate(View):
    def get(self, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk = uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(self.request, user)
            return redirect('signin')
        else:
            messages.warning(self.request, _('unfortunately we couldn\'t activate your accounts.'))
            return redirect('signin')

class ProfilePassenger(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):    
        basic_form = UserBasicForm(instance = request.user)
        general_form = GeneralProfileForm(instance = request.user.profile)
        passenger_form = PassengerProfileForm(instance = request.user.profile.passenger)

        return render(self.request, "dashboard/passenger/passenger-profile.html", context = {'basic_form': basic_form, 'passenger_form': passenger_form, 'general_form': general_form, 'category': 'passenger'})

    def post(self, request, *args, **kwargs):

        basic_form = UserBasicForm(request.POST, instance = request.user)
        general_form = GeneralProfileForm(request.POST, request.FILES, instance = request.user.profile)
        passenger_form = PassengerProfileForm(request.POST, instance = request.user.profile.passenger)

        if basic_form.is_valid():
            basic_form.save()
        if general_form.is_valid():
            general_form.save()
        if passenger_form.is_valid():
            passenger_form.save()
        
        if not basic_form.is_valid() or not passenger_form.is_valid() or not general_form.is_valid():
            return render(self.request, "dashboard/passenger/passenger-profile.html", context = {'basic_form': basic_form, 'passenger_form': passenger_form, 'general_form': general_form, 'category': 'passenger'})

        return redirect("dashboard:passenger-profile")

class ProfileDriver(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):    
        basic_form = UserBasicForm(instance = request.user)
        general_form = GeneralProfileForm(instance = request.user.profile)
        driver_form = DriverProfileForm(instance = request.user.profile.driver)
        driver_bank_form = DriverBankProfileForm(instance = request.user.profile.driver.bank)
        driver_machine_form = DriverMachineProfileForm(instance = request.user.profile.driver.machine)

        return render(self.request, "dashboard/driver/driver-profile.html", context = {'basic_form': basic_form, 'general_form': general_form, 'driver_form': driver_form, 'driver_bank_form': driver_bank_form, 'driver_machine_form': driver_machine_form, 'category': 'driver'})

    def post(self, request, *args, **kwargs):

        basic_form = UserBasicForm(request.POST, instance = request.user)
        general_form = GeneralProfileForm(request.POST, request.FILES, instance = request.user.profile)
        driver_form = DriverProfileForm(request.POST, instance = request.user.profile.driver)
        driver_bank_form = DriverBankProfileForm(request.POST, instance = request.user.profile.driver.bank)
        driver_machine_form = DriverMachineProfileForm(request.POST, request.FILES, instance = request.user.profile.driver.machine)

        if basic_form.is_valid():
            basic_form.save()
        if general_form.is_valid():
            general_form.save()
        if driver_form.is_valid():
            driver_form.save()
        if driver_bank_form.is_valid():
            driver_bank_form.save()
        if driver_machine_form.is_valid():
            driver_machine_form.save()
        
        if not basic_form.is_valid() or not driver_form.is_valid() or not general_form.is_valid() or not driver_bank_form.is_valid() or not driver_machine_form.is_valid():
            return render(self.request, "dashboard/driver/driver-profile.html", context = {'basic_form': basic_form, 'general_form': general_form, 'driver_form': driver_form, 'driver_bank_form': driver_bank_form, 'driver_machine_form': driver_machine_form, 'category': 'driver'})

        return redirect("dashboard:driver-profile")

class ProfileTransmit(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):    
        basic_form = UserBasicForm(instance = request.user)
        general_form = GeneralProfileForm(instance = request.user.profile)
        transmit_form = TransmitProfileForm(instance = request.user.profile.transmit)

        return render(self.request, "profile-transmit.html", context = {'basic_form': basic_form, 'transmit_form': transmit_form, 'general_form': general_form})

    def post(self, request, *args, **kwargs):

        basic_form = UserBasicForm(request.POST, instance = request.user)
        general_form = GeneralProfileForm(request.POST, request.FILES, instance = request.user.profile)
        transmit_form = TransmitProfileForm(request.POST, instance = request.user.profile.transmit)

        if basic_form.is_valid():
            basic_form.save()
        if general_form.is_valid():
            general_form.save()
        if transmit_form.is_valid():
            transmit_form.save()
        
        if not basic_form.is_valid() or not transmit_form.is_valid() or not general_form.is_valid():
            return render(self.request, "profile-transmit.html", context = {'basic_form': basic_form, 'transmit_form': transmit_form, 'general_form': general_form})

        return redirect("profile-transmit")