from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import lugar_data
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.

def detail_lugar(request, lugar_id):
    lugar = lugar_data[lugar_id - 1]
    return HttpResponse(
        f'Detalhes do lugar {lugar["name"]} ({lugar["description"]})')

def list_lugares(request):
    context = {"lugar_list": lugar_data}
    return render(request, 'lugares/index.html', context)

def detail_lugar(request, lugar_id):
    lugar = get_object_or_404( Post , pk=lugar_id)
    context = {'lugar': lugar}
    return render(request, 'lugares/detail.html', context)


def search_lugares(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        lugar_list = Post.objects.filter(name__icontains=search_term)
        context = {"lugar_list": lugar_list}
    return render(request, 'lugares/search.html', context)



def create_lugar(request):
    if request.method == 'POST':
        lugar_name = request.POST['name']
        lugar_description = request.POST['description']
        lugar_poster_url = request.POST['poster_url']
        lugar_content = request.POST['content']
        lugar = Post(name=lugar_name,
                      description = lugar_description,
                      poster_url = lugar_poster_url,
                      content = lugar_content
                      )
        lugar.save()
        return HttpResponseRedirect(
            reverse('lugares:detail', args=(lugar.id, )))
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'lugares/create.html', context)

    
def list_lugares(request):
    lugar_list = Post.objects.all()
    context = {'lugar_list': lugar_list}
    return render(request, 'lugares/index.html', context)

def update_lugar(request, lugar_id):
    lugar = get_object_or_404(Post, pk=lugar_id)

    if request.method == "POST":
        lugar.name = request.POST['name']
        lugar.description = request.POST['description']
        lugar.content = request.POST['content']
        lugar.poster_url = request.POST['poster_url']
        lugar.save()
        return HttpResponseRedirect(
            reverse('lugares:detail', args=(lugar.id, )))

    context = {'lugar': lugar}
    return render(request, 'lugares/update.html', context)


def delete_lugar(request, lugar_id):
    lugar = get_object_or_404(Post, pk=lugar_id)

    if request.method == "POST":
        lugar.delete()
        return HttpResponseRedirect(reverse('lugares:index'))

    context = {'lugar': lugar}
    return render(request, 'lugares/delete.html', context)