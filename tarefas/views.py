from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Tarefa
from usuarios.models import Usuario

# View para listar todas as tarefas
def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('usuario_responsavel').all()
    
    # Filtro por status se fornecido
    status = request.GET.get('status')
    if status:
        tarefas = tarefas.filter(status=status)
    
    contexto = {
        'tarefas': tarefas,
        'status_choices': Tarefa.STATUS_CHOICES
    }
    return render(request, 'tarefas/listar.html', contexto)

# View para exibir detalhes de uma tarefa
def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

# View para criar uma nova tarefa
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade', 1)
        data_vencimento = request.POST.get('data_vencimento')
        usuario_id = request.POST.get('usuario_responsavel')
        
        usuario = None
        if usuario_id:
            usuario = get_object_or_404(Usuario, id=usuario_id, ativo=True)
        
        tarefa = Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            data_vencimento=data_vencimento if data_vencimento else None,
            usuario_responsavel=usuario
        )
        messages.success(request, f'Tarefa "{tarefa.titulo}" criada com sucesso!')
        return redirect('listar_tarefas')
    
    usuarios = Usuario.objects.filter(ativo=True)
    return render(request, 'tarefas/criar.html', {'usuarios': usuarios})

# View para atualizar uma tarefa
def atualizar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.prioridade = request.POST.get('prioridade')
        tarefa.data_vencimento = request.POST.get('data_vencimento') or None
        tarefa.concluida = request.POST.get('concluida') == 'on'
        
        usuario_id = request.POST.get('usuario_responsavel')
        if usuario_id:
            tarefa.usuario_responsavel = get_object_or_404(Usuario, id=usuario_id, ativo=True)
        else:
            tarefa.usuario_responsavel = None
        
        tarefa.save()
        
        messages.success(request, f'Tarefa "{tarefa.titulo}" atualizada com sucesso!')
        return redirect('detalhe_tarefa', pk=tarefa.pk)
    
    usuarios = Usuario.objects.filter(ativo=True)
    return render(request, 'tarefas/atualizar.html', {'tarefa': tarefa, 'usuarios': usuarios})

# View para deletar uma tarefa
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        titulo = tarefa.titulo
        tarefa.delete()
        messages.success(request, f'Tarefa "{titulo}" deletada com sucesso!')
        return redirect('listar_tarefas')
    
    return render(request, 'tarefas/deletar.html', {'tarefa': tarefa})

# View para marcar como concluída
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = True
    tarefa.status = 'concluida'
    tarefa.save()
    messages.success(request, f'Tarefa "{tarefa.titulo}" marcada como concluída!')
    return redirect('detalhe_tarefa', pk=pk)

# View para mudar status
def mudar_status(request, pk):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, pk=pk)
        novo_status = request.POST.get('status')
        tarefa.status = novo_status
        if novo_status == 'concluida':
            tarefa.concluida = True
        tarefa.save()
        messages.success(request, f'Status atualizado para "{novo_status}"!')
    return redirect('listar_tarefas')
