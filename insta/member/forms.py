from django import forms
from django.contrib.auth.models import User  # Django 내장모델인 'User'를 import
from django.contrib.auth.forms import UserCreationForm  # Django 내장 form인 UserCreationForm 을 import

# Django의 내장 form인 UserCreationForm를 상속하여 UserCreateForm 클래스를 작성

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "username")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    # Help메시지가 표시되지 않도록 수정
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
