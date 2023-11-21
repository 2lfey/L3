from django.urls import reverse_lazy
from django.views import generic as generic_views

from . import models
from . import forms

# Create your views here.


class PostListView(generic_views.ListView):
    model = models.Post
    context_object_name = "posts"
    template_name = 'posts.html'


class CreatePostView(generic_views.CreateView):
    form_class = forms.CreatePostForm
    success_url = reverse_lazy('user-profile')
    template_name = 'create_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        kwargs['user'] = self.request.user

        return kwargs
