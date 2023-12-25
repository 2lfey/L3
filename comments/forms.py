from django import forms

from posts import models as post_models

from . import models


class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=2000, widget=forms.Textarea, required=True)

    class Meta():
        model = models.Comment
        fields = (
            'content',
            'image',
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')

        if self.request is None:
            raise Exception('No request in form')

        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)

        comment.post = post_models.Post.objects.get(
            id=self.request.resolver_match.kwargs['pk'])
        comment.author = self.request.user

        if commit:
            comment.save(True)

        return comment
