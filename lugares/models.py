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

