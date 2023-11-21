from django import forms

from . import models


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Post
        fields = (
            'image',
            'hashtags',
            'content',
        )

    def clean(self):
        self.cleaned_data['author_id'] = self.user.id
        super().clean()

    def save(self, commit=True):
        post = super().save()
        
        post.author.id = self.cleaned_data['author_id']

        if commit:
            post.save()

        return post
