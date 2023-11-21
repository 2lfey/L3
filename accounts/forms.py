from django import forms
from django.core.validators import ValidationError

from . import models


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('username', 'password', 'password2')

    def clean(self):
        super().clean()

        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    summary = forms.CharField(
        max_length=2000, widget=forms.Textarea, required=False)

    class Meta:
        model = models.User
        fields = ('avatar', 'summary')

    def clean(self):
        super().clean()

        avatar = self.cleaned_data.get('avatar')

        # If avatar large then 10mb
        if not avatar and avatar.size > 1024 * 1024 * 10:
            raise ValidationError('large_image')

    def save(self, commit=True):
        user = super().save(commit=False)
        avatar = self.cleaned_data.get('avatar')
        
        # If avatar exist add it
        if avatar:
            user.avatar = avatar

        if commit:
            user.save()

        return user
