from typing import Any
from django.urls import reverse_lazy
from django.views import generic as generic_views

from comments import models as comments_models

from . import models
from . import forms

# Create your views here.


class PostListView(generic_views.ListView):
    model = models.Post
    context_object_name = "posts"
    template_name = 'posts.html'


class CreatePostView(generic_views.CreateView):
    form_class = forms.CreatePostForm
    template_name = 'create_post.html'

    def get_success_url(self) -> str:
        return reverse_lazy('user-profile', kwargs={'pk': self.request.user.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs


class PostDetailView(generic_views.DetailView):
    model = models.Post
    template_name = 'detail_post.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)

        data['comments'] = comments_models.Comment.get_comments_by_post(
            models.Post.objects.get(
                id=self.request.resolver_match.kwargs['pk'])
        )

        return data
