from enum import Enum

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import AuthUser


class ErrorMessages(str, Enum):
    EMAIL_ALREADY_EXIST = 'Email уже зарегистрирован!'
    PASSWORDS_SYNC_CONFIRM = 'Пароли не совпадают, пожалуйста, введите пароли еще раз!'

    def __str__(self) -> str:
        return str.__str__(self)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(ErrorMessages.PASSWORDS_SYNC_CONFIRM)

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if AuthUser.objects.filter(email=email).exists():
            raise forms.ValidationError(ErrorMessages.EMAIL_ALREADY_EXIST)
        return email

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass
