from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'livros/',
        views.lista_livros,
        name='lista_livros'
    ),

    path(
        'novo/',
        views.criar_livro,
        name='criar_livro'
    ),

    path(
        'editar/<int:pk>/',
        views.editar_livro,
        name='editar_livro'
    ),

    path(
        'excluir/<int:pk>/',
        views.excluir_livro,
        name='excluir_livro'
    ),
]