from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'description',
            'content',
            'poster_url',
        ]
        labels = {
            'name': 'Nome',
            'descrption': 'Descrição',
            'content' : 'Sobre',
            'poster_url': 'URL do Poster',
        }