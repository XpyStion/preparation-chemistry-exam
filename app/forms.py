from enum import Enum
from os import getenv

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .core.prompt import Prompt
from .core.yandex_gpt_client import YandexGPTClient
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


class CreateTaskForm(forms.Form):
    selected_task = forms.CharField(widget=forms.Textarea)

    def create_task_with_prompt(self):
        prompt = Prompt()
        selected_task = self.cleaned_data.get('selected_task')
        method = f"get_{selected_task.replace('-', '_')}_prompt"

        task_text = YandexGPTClient(
            token=getenv('OAUTH_TOKEN'),
            folder_id=getenv('FOLDER_ID')
        ).get_prompt_response_msg(
            text=getattr(prompt, method)
        )
        return {
            'task_text': task_text,
            'selected_task': selected_task
        }
