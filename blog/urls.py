from django.urls import path

from blog.views import (editar_categoria, excluir_categoria, index,
                        inserir_categoria, post_categoria,
                        visualizar_categorias, visualizar_post)

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', visualizar_post, name='visualizar_post'),
    path('post/<categoria>/', post_categoria, name='post_categoria'),
    path('inserir_categoria/', inserir_categoria, name='inserir_categoria'),
    path('visualizar_categorias/', visualizar_categorias, name='visualizar_categorias'),
    path('editar_categoria/<int:id>', editar_categoria, name='editar_categoria'),
    path('excluir_categoria/<int:id>', excluir_categoria, name='excluir_categoria'),
]
