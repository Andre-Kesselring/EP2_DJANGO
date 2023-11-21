from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }