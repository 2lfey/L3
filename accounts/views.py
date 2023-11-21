# from django.shortcuts import render
from django.views import generic as generic_views
from django.urls import reverse_lazy

from . import models
from . import forms

# Create your views here.


class RegisterView(generic_views.CreateView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')


class ProfileView(generic_views.UpdateView):
    template_name = 'profile.html'
    # model = models.User
    # fields = ['avatar', 'summary']
    form_class = forms.ProfileForm
    context_object_name = "obj"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class UserProfileView(generic_views.DetailView):
    model = models.User
    context_object_name = "obj"
    template_name = 'user_profile.html'
