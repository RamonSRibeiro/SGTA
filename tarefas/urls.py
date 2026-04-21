from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    
    path('tarefa/<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    
    path('tarefa/<int:pk>/atualizar/', views.atualizar_tarefa, name='atualizar_tarefa'),
    
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    
    path('tarefa/<int:pk>/status/', views.mudar_status, name='mudar_status'),
]
