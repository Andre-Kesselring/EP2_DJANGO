from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import lugar_data
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'lugares/index.html'
    context_object_name = 'lugar_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Lugares'
        context['lugarpage_title'] = 'Encontre o lugar ideal!!!!!!!!!!!!!!!!!!'
        context['category'] = False
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'lugares/detail.html'
    context_object_name = 'lugar'

class PostSearchView(ListView):
    model = Post
    template_name = 'lugares/search.html'
    context_object_name = 'lugar_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Post.objects.filter(name__icontains=query.lower())
        else:
            return Post.objects.none()

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'lugares/create.html'
    success_url = reverse_lazy('lugares:create')

    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(reverse('lugares:detail', args=(self.object.id,)))

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'lugares/update.html'
    context_object_name = 'lugar'

    def get_success_url(self):
        return reverse_lazy('lugares:detail', args=(self.object.id,))

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'lugares/delete.html'
    context_object_name = 'lugar'
    success_url = reverse_lazy('lugares:index')

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('lugares:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'lugares/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'lugares/category.html'
    context_object_name = 'category_list'

class CategoryPostsListView(generic.ListView):
    template_name = 'lugares/index.html'
    context_object_name = 'lugar_list'

    def get_category(self):
        return Category.objects.get(pk=self.kwargs['category_id'])

    def get_queryset(self):
        return self.get_category().posts.all()
    
    def get_context_data(self, **kwargs):
        category = self.get_category()
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Categoria'
        context['lugarpage_title'] = f'Categoria {category.name}'
        context['category'] = True
        context['category_id'] = category.id
        return context

class CategoryPostDetailView(generic.DetailView):
    model = Post
    template_name = 'lugares/detail.html'

    def get_object(self):
        category_id = self.kwargs.get('category_id')
        pk = self.kwargs.get('pk')
        category = Category.objects.get(pk=category_id)
        posts = category.posts.all()
        post = get_object_or_404(posts, pk=pk) 
        return post