from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Livro, Autor

def listagem_livros(request):
    context = {'livros': Livro.objects.all()}
    return render(request, 'Livros/listagem_livros.html', context)

def detalhes_livro(request, id):
    livro = Livro.objects.get(id=id)
    context = {'livro': livro}
    return render(request, 'Livros/detalhes_livro.html', context)

def listagem_autores(request):
    context = {'autores': Autor.objects.all()}
    return render(request, 'Livros/listagem_autores.html', context)

def detalhes_autor(request, id):
    autor = Autor.objects.get(id=id)
    context = {'autor': autor}
    return render(request, 'Livros/detalhes_autor.html', context)