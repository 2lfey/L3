from django.urls import reverse_lazy
from django.views import generic as generic_views

from posts import models as post_models

from . import models
from . import forms

# Create your views here.


class CreateComment(generic_views.CreateView):
    form_class = forms.CreateCommentForm
    template_name = 'create_comment.html'

    def get_queryset(self):
        return post_models.Post.objects.get_queryset()

    def get_success_url(self) -> str:
        return reverse_lazy('detail-post', kwargs={'pk': self.request.resolver_match.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['request'] = self.request

        return kwargs


class DeleteComment(generic_views.DeleteView):
    model = models.Comment
    template_name = 'delete_comment.html'

    def get_success_url(self) -> str:
        return reverse_lazy('detail-post', kwargs={'pk': self.request.resolver_match.kwargs['pk']})


class DeleteComment(generic_views.DeleteView):
    model = models.Comment
    template_name = 'delete_comment.html'

    def get_success_url(self) -> str:
        return reverse_lazy('detail-post', kwargs={'pk': self.request.resolver_match.kwargs['post_pk']})


class UpdateComment(generic_views.UpdateView):
    model = models.Comment
    fields = ('content', 'image',)
    template_name = 'update_comment.html'

    def get_success_url(self) -> str:
        return reverse_lazy('detail-post', kwargs={'pk': self.request.resolver_match.kwargs['post_pk']})
