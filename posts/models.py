from django.db import models

from django.utils.timezone import utc

from datetime import datetime

# Create your models here.


class Hashtag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) :
        return self.name


class Post(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    content = models.TextField(max_length=10000, blank=True)
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
                # November 00:00
                return self.created_at.strftime('Edited %B %H:%M')
            else:
                # 2023 November 00:00
                return self.created_at.strftime('Edited %Y %B %H:%M')
        else:
            diff = (now - self.created_at)
            if diff.days == 0:
                # Today 00:00
                return self.created_at.strftime('Today %H:%M')
            elif diff.days < 7:
                # Monday 00:00
                return self.created_at.strftime('%A %H:%M')
            elif diff.days < 365:
                # November 00:00
                return self.created_at.strftime('%B %H:%M')
            else:
                # 2023 November 00:00
                return self.created_at.strftime('%Y %B %H:%M')

    def __str__(self) -> str:
        return self.content