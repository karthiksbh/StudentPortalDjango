from typing import List
from django.forms.models import ModelForm
from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from app.models import StudentProfile, todo_list
from django.contrib.auth import password_validation


class User_Register(UserCreationForm):
    password1 = forms.CharField(
        label='Create Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control'})}


class User_Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class Studentprofile(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student_name', 'class_student',
                  'student_email', 'mobile_number', 'school', 'city']
        widgets = {'student_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'class_student': forms.Select(attrs={'class': 'form-control'}),
                   'student_email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'school': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'})}


class Todo_Form(forms.ModelForm):

    desc = forms.CharField(
        label='Enter Your Todo', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = todo_list
        fields = ['desc']


class Password_Change(PasswordChangeForm):
    old_password = forms.CharField(label=_("Enter Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("Enter New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class Password_Reset(PasswordResetForm):
    email = forms.EmailField(label=_("Enter Your Email"), max_length=250, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class Password_Set(SetPasswordForm):
    new_password1 = forms.CharField(label=_("Enter New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
