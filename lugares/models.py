from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    poster_url = models.URLField(max_length=200, null=True)
    content = models.TextField(default="")
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"{self.name}" - {self.description}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"{self.text}" - {self.author.username} em {self.date}'