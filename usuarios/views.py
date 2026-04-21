from django.shortcuts import render, get_object_or_404
from .models import Usuario

def listar_usuarios(request):
    """Lista todos os usuários ativos"""
    usuarios = Usuario.objects.filter(ativo=True)
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

def buscar_usuario_por_id(request, id):
    """Busca um usuário por ID"""
    usuario = get_object_or_404(Usuario, id=id, ativo=True)
    return render(request, 'usuarios/detalhe.html', {'usuario': usuario})
