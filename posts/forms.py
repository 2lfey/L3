from django import forms

from . import models


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        if self.user is None:
            raise Exception('No user in form')

        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Post
        fields = (
            'image',
            # 'hashtags',
            'content',
        )

    def save(self, commit=True):
        post = super().save(commit=False)

        post.author = self.user

        if commit:
            post.save()

        return post
