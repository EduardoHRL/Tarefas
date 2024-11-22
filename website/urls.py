from django.contrib import admin
from django.urls import include, path
from website import views

urlpatterns = [
    path('', views.logar, name='logar'),

    path('index/', views.index, name='index'),

    path('cadastro/', views.cadastro, name='cadastro'),

    path('tarefas/', views.TarefaListView.as_view(), name='lista_tarefas'),

    path('tarefa/cadastrar', views.TarefaCreateView.as_view(), name='cadastra_tarefa'),

    path('tarefa/excluir/<int:pk>', views.TarefaDeleteView.as_view(), name='deleta_tarefa'),

    path('atualiza_status/<int:pk>/', views.atualiza_status, name='atualiza_status'),
]