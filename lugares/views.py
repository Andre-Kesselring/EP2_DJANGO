from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import lugar_data
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def detail_lugar(request, lugar_id):
    lugar = lugar_data[lugar_id - 1]
    return HttpResponse(
        f'Detalhes do lugar {lugar["name"]} ({lugar["description"]})')

def list_lugares(request):
    context = {"lugar_list": lugar_data}
    return render(request, 'lugares/index.html', context)

def detail_lugar(request, lugar_id):
    context = {'lugar': lugar_data[lugar_id - 1]}
    return render(request, 'lugares/detail.html', context)

def search_lugares(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "lugar_list": [
                m for m in lugar_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'lugares/search.html', context) # modifique esta linha



def create_lugar(request):
    if request.method == 'POST':
        lugar_data.append({
            'name': request.POST['name'],
            'description': request.POST['description'],
            'image_url': request.POST['image_url']
        })
        return HttpResponseRedirect(
            reverse('lugares:detail', args=(len(lugar_data), )))
    else:
        return render(request, 'lugares/create.html', {})