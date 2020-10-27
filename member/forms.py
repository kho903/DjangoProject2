from django import forms
from django.contrib.auth.models import User  # Django 내장모델인 'User'를 import
from django.contrib.auth.forms import UserCreationForm, \
    ReadOnlyPasswordHashField, UserChangeForm  # Django 내장 form인 UserCreationForm 을 import


# Django의 내장 form인 UserCreationForm를 상속하여 UserCreateForm 클래스를 작성
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User

#
# class UserCreationForm(forms.ModelForm):
#     # 사용자 생성 폼
#     email = forms.EmailField(
#         label=_('Email'),
#         required=True,
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Email address'),
#                 'required': 'True',
#             }
#         )
#     )
#     nickname = forms.CharField(
#         label=_('Nickname'),
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Nickname'),
#                 'required': 'True',
#             }
#         )
#     )
#     password1 = forms.CharField(
#         label=_('Password'),
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Password'),
#                 'required': 'True',
#             }
#         )
#     )
#     password2 = forms.CharField(
#         label=_('Password confirmation'),
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Password confirmation'),
#                 'required': 'True',
#             }
#         )
#     )
#
#     class Meta:
#         model = User
#         fields = ('email', 'nickname')
#
#     def clean_password2(self):
#         # 두 비밀번호 입력 일치 확인
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = UserManager.normalize_email(self.cleaned_data['email'])
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     # 비밀번호 변경 폼
#     password = ReadOnlyPasswordHashField(
#         label=_('Password')
#     )
#
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'is_active', 'is_superuser')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]



## user
#

# 회원가입 폼
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


# 업데이트 폼
class UserUpdateForm(UserChangeForm):

    password = ReadOnlyPasswordHashField()

    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password', 'birth_date', 'image','text')

    widgets={
        'email' : forms.TextInput(),
        'birth_date' : forms.DateTimeField(),
        'text' : forms.Textarea(attrs={'rows':3}),
        'username' : forms.TextInput(attrs={'readonly':'readonly'})
    }

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def _clean_fields(self):
        return