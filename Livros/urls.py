from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.listagem_livros, name='listaLivros'),
    path('livros/<int:id>/', views.detalhes_livro, name='detalhesLivro'),
    path('autores/', views.listagem_autores, name='listaAutores'),
    path('autores/<int:id>/', views.detalhes_autor, name='detalhesAutor'),
]