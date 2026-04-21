from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('<int:id>/', views.buscar_usuario_por_id, name='detalhe_usuario'),
]
