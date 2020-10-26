from django import forms
from django.contrib.auth.models import User  # Django 내장모델인 'User'를 import
from django.contrib.auth.forms import UserCreationForm, \
    ReadOnlyPasswordHashField  # Django 내장 form인 UserCreationForm 을 import


# Django의 내장 form인 UserCreationForm를 상속하여 UserCreateForm 클래스를 작성
from django.core.exceptions import ValidationError


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "username")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't Match")
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    # Help 메시지가 표시되지 않도록 수정
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


# 비밀 번호 변경 폼.
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def _clean_fields(self):
        return