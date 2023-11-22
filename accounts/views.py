# from django.shortcuts import render
from typing import Any, Dict
from django.views import generic as generic_views
from django.urls import reverse_lazy

from posts import models as posts_models

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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        
        data['posts'] = posts_models.Post.objects.filter(author=self.request.user).order_by('-created_at')
        
        print(data)
        
        return data
