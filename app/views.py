from django.shortcuts import render, redirect

from app.base.views_base import ViewBase
from app.forms import UserRegistrationForm


class MainPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'main_page/main_page.html')


class UserRegistrationPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'patch', 'delete')
    INVALID_FORM_ERROR: str = 'Invalid form data provided'

    @staticmethod
    def get(request):
        form = UserRegistrationForm()
        return render(request, 'account/register_user.html', {'form': form})

    @staticmethod
    def post(request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
        return render(request, 'account/register_user.html', {'form': form})


class TrainVariationsPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'train_variations/train_variations.html')


class MaterialsPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'materials/materials.html')


class SearchPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'search/search.html')


class ForumPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'forum/forum.html')


class AccountPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'account/account.html')


class LoginPageView(ViewBase):
    PROHIBITED_METHODS: tuple = ('put', 'post', 'patch', 'delete')

    @staticmethod
    def get(request):
        return render(request, 'account/login.html')
