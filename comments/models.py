from django.db import models
from django.utils.timezone import utc

from datetime import datetime

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='comments', blank=True)
    content = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def time(self):
        now = datetime.utcnow().replace(tzinfo=utc)

        if (self.updated_at - self.created_at).seconds > 3:
            diff = (now - self.updated_at)
            if diff.days == 0:
                # Today 00:00
                return self.created_at.strftime('Edited today %H:%M')
            elif diff.days < 7:
                # Monday 00:00
                return self.created_at.strftime('Edited %A %H:%M')
            elif diff.days < 365:
                # November 1 00:00
                return self.created_at.strftime('Edited %B %-d %H:%M')
            else:
                # 2023 November 1 00:00
                return self.created_at.strftime('Edited %Y %B %-d %H:%M')
        else:
            diff = (now - self.created_at)
            if diff.days == 0:
                # Today 00:00
                return self.created_at.strftime('Today %H:%M')
            elif diff.days < 7:
                # Monday 00:00
                return self.created_at.strftime('%A %H:%M')
            elif diff.days < 365:
                # November 1 00:00
                return self.created_at.strftime('%B %-d %H:%M')
            else:
                # 2023 November 1 00:00
                return self.created_at.strftime('%Y %B %-d %H:%M')

    def __str__(self) -> str:
        return self.content

    @staticmethod
    def get_comments_by_post(post):
        return Comment.objects.filter(post=post)
