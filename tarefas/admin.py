from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'data_criacao', 'concluida')
    list_filter = ('status', 'concluida', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    ordering = ('-data_criacao',)
    readonly_fields = ('data_criacao', 'data_atualizacao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao')
        }),
        ('Status', {
            'fields': ('status', 'concluida', 'prioridade')
        }),
        ('Datas', {
            'fields': ('data_vencimento', 'data_criacao', 'data_atualizacao')
        }),
    )
