from django.shortcuts import render, redirect

from app.base.views_base import ViewBase
from app.forms import UserRegistrationForm


class UserRegistrationView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')
    INVALID_FORM_ERROR: str = 'Invalid form data provided'

    @staticmethod
    def get(request):
        form = UserRegistrationForm()
        return render(request, 'register_user.html', {'form': form})

    @staticmethod
    def post(request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
        return render(request, 'register_user.html', {'form': form})
