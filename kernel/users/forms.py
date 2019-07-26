from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from users.models import GeneralProfile
from users.models import Passenger
from users.models import Transmit
from users.models import Driver
from users.models import Machine
from users.models import Bank

from painless.models.validations import validate_charachters
from painless.models.validations import validate_phone_number
from painless.models.validations import validate_national_code
from painless.models.validations import validate_postal_code
from painless.models.validations import validate_plaque
from painless.models.validations import validate_bank_names
from painless.models.validations import validate_bank_iban
from painless.models.validations import validate_bank_card

YEARS = [year for year in range(1300, 1400)]
MONTHS = {
        1:_('فروردین'), 2:_('اردیبهشت'), 3:_('خرداد'), 
        4:_('تیر'), 5:_('مرداد'), 6:_('شهریور'), 
        7:_('مهر'), 8:_('آبان'), 9:_('آذر'), 
        10:_('دی'), 11:_('بهمن'), 12:_('اسفند')
    }

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label = 'ایمیل', required = True)
    password = forms.CharField(label = 'رمز عبور',widget = forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = 'ایمیل', max_length=30, required = True)
    first_name = forms.CharField(label = 'نام', max_length=30, required = True, help_text = 'enter your first name.')
    last_name = forms.CharField(label = 'نام خانوادگی', max_length=30, required = True)
    phone_number = forms.CharField(label = 'شماره تماس', max_length=30, required = True)
    password1 = forms.CharField(label = 'رمز عبور', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'تکرار رمز عبور', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

class GeneralProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years= YEARS, months=MONTHS), label = _('تاریخ تولد'))
    tel = forms.CharField(validators = [validate_phone_number], label = _('شماره تلفن'), required = True)
    mobile = forms.CharField(validators = [validate_phone_number], label = _('شماره موبایل'), required = True)
    national_code = forms.CharField(validators = [validate_national_code], label = _('کد ملی'), required = True)
    postal_code = forms.CharField(validators = [validate_postal_code], label = _('کد پستی'), required = True)
    adr = forms.CharField(label = _('آدرس'), required = True)
    pic = forms.ImageField(label = _('عکس'), required = True)
    national_code_pic = forms.ImageField(label = _('عکس کد ملی'), required = True)
    edu_degree = forms.ChoiceField(choices = GeneralProfile.DEGREES, label = _('مدرک تحصیلی'), required = True)

    class Meta:
        model = GeneralProfile
        fields = ('gender', 'birth_date', 'tel', 'national_code', 'mobile', 'adr', 'postal_code', 'pic', 'national_code_pic', 'edu_degree' )
  

    def __init__(self, *args, **kwargs):
        super(GeneralProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
        
class PassengerProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PassengerProfileForm, self).__init__(*args, **kwargs)
        phone_num = self.fields['emergency_number']
        phone_num.validators.append(validate_phone_number)

    
    class Meta:
        model = Passenger
        fields = ('job', 'emergency_number')

        labels = {
            'job': _('شغل'),
            'emergency_number': _('شماره تماس ضروری')
        }

class DriverProfileForm(forms.ModelForm):
    job = forms.CharField(validators = [validate_charachters ], required = True, label = _('شغل'))
    job_place = forms.CharField(validators = [validate_charachters ], required = True, label = _('محل شغل'))
    emergency_number = forms.CharField(validators = [validate_phone_number],required = True, label = _('شماره ضروری'))
    def __init__(self, *args, **kwargs):
        super(DriverProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
        phone_num = self.fields['emergency_number']
        phone_num.validators.append(validate_phone_number)
    
    class Meta:
        model = Driver
        fields = ('job', 'job_place', 'emergency_number')
        labels = {
            'job': _('شغل'),
            'job_place': _('محل شغل'),
            'emergency_number': _('شماره تماس ضروری')
        }

class DriverMachineProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=20, validators=[validate_charachters], required = True, label=_('نام'))
    color = forms.CharField(max_length=20, validators=[validate_charachters], required = True, label = _('رنگ'))
    model = forms.CharField(max_length=20, validators=[validate_charachters], required = True, label = _('مدل'))
    plaque = forms.CharField(max_length=8, validators =[validate_plaque], required = True, label = _('پلاک'))
    year = forms.DateField(widget=forms.SelectDateWidget(years= YEARS, months=MONTHS), required = True, label = _('سال'))
    chassis_number = forms.CharField(max_length=17, min_length=17, required = True, label = _('شماره شاسی'))

    def __init__(self, *args, **kwargs):
        super(DriverMachineProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
    
    class Meta:
        model = Machine
        fields = ('name', 'color', 'model', 'plaque', 'year', 'chassis_number', 'driver_card', 'machine_card', 'misdiagnosis', 'car_pic')

class DriverBankProfileForm(forms.ModelForm):
    bank_acc_name = forms.CharField(validators = [validate_charachters],required = True, label = _('نام دارنده حساب بانکی'))
    bank_name = forms.CharField(validators = [validate_bank_names],required = True, label = _('نام بانک'))
    bank_sheba = forms.CharField(validators = [validate_bank_iban],required = True, label = _('شماره شبا بانکی'))
    bank_card = forms.CharField(validators = [validate_bank_card], required = True, label = _('شماره کارت بانکی'))
    
    def __init__(self, *args, **kwargs):
        super(DriverBankProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
    
    class Meta:
        model = Bank
        fields = ('bank_acc_name', 'bank_name', 'bank_sheba', 'bank_card')

class UserBasicForm(forms.ModelForm):
    first_name = forms.CharField(max_length=16, validators = [validate_charachters], label = _('نام'))
    last_name = forms.CharField(max_length=16, validators = [validate_charachters], label = _('نام خانوادگی'))

    def __init__(self, *args, **kwargs):
        super(UserBasicForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.required = True
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
    
class TransmitProfileForm(forms.ModelForm):
    job = forms.CharField(validators = [validate_charachters ], required = True, label = _('شغل'))
    emergency_number = forms.CharField(validators = [validate_phone_number],required = True, label = _('شماره ضروری'))
    
    def __init__(self, *args, **kwargs):
        super(TransmitProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': _('فیلد {} اجباری است.'.format(field.label))
            }
    
    class Meta:
        model = Transmit
        fields = ('job', 'emergency_number')