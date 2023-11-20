from django.db import models
from django.conf import settings

# Create your models here.

class Lugar(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.description})'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'