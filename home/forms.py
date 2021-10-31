from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import  ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Tài khoản', max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Mật khẩu không hợp lệ')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có ký tự đặc biệt')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')
        
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])