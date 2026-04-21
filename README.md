# 📋 Gerenciador de Tarefas com Usuários - Documentação

## 📦 O que foi criado

Um app completo de gerenciamento de tarefas em Django com sistema de usuários responsáveis:

### Models
#### Tarefa
- `titulo`: Título da tarefa (obrigatório)
- `descricao`: Descrição detalhada (opcional)
- `status`: Pendente, Em Progresso ou Concluída
- `prioridade`: 1 (Baixa), 2 (Média) ou 3 (Alta)
- `data_criacao`: Data de criação automática
- `data_atualizacao`: Última atualização automática
- `data_vencimento`: Data para vencer (opcional)
- `concluida`: Flag de conclusão
- `usuario_responsavel`: ForeignKey para Usuario (SET_NULL, opcional)

#### Usuario (NOVO!)
- `nome`: Nome do usuário
- `email`: Email único
- `ativo`: Status ativo/inativo (padrão: True)
- `data_criacao`: Data de criação automática

### Views (Rotas)
#### Tarefas
- **GET /tarefas/**: Listar todas as tarefas com filtro por status
- **GET /tarefas/tarefa/<id>/**: Ver detalhes de uma tarefa
- **GET/POST /tarefas/criar/**: Criar nova tarefa (com seleção de responsável)
- **GET/POST /tarefas/tarefa/<id>/atualizar/**: Atualizar tarefa
- **GET/POST /tarefas/tarefa/<id>/deletar/**: Deletar tarefa
- **POST /tarefas/tarefa/<id>/concluir/**: Marcar como concluída
- **POST /tarefas/tarefa/<id>/status/**: Mudar status

#### Usuários (NOVO!)
- **GET /usuarios/**: Listar todos os usuários ativos
- **GET /usuarios/<id>/**: Ver detalhes de um usuário com suas tarefas

### Templates
#### Tarefas
- `listar.html`: Lista tarefas com filtro (agora mostra responsável)
- `detalhe.html`: Detalhes da tarefa (mostra responsável + link)
- `criar.html`: Formulário para criar tarefa (com seleção de responsável)
- `atualizar.html`: Formulário para editar tarefa (com seleção de responsável)
- `deletar.html`: Confirmação antes de deletar

#### Usuários (NOVO!)
- `listar.html`: Lista de todos os usuários ativos
- `detalhe.html`: Perfil do usuário com tarefas atribuídas

## 🚀 Como executar

### 1. Criar migrações do banco de dados
```bash
python manage.py makemigrations
```

### 2. Aplicar as migrações
```bash
python manage.py migrate
```

### 3. Criar um superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
```

### 4. Executar o servidor
```bash
python manage.py runserver
```

### 5. Acessar a aplicação
- **App de tarefas**: http://127.0.0.1:8000/tarefas/
- **App de usuários**: http://127.0.0.1:8000/usuarios/
- **Admin Django**: http://127.0.0.1:8000/admin/

## 📝 Como usar

### Criar um Usuário
1. Acesse http://127.0.0.1:8000/admin/
2. Clique em "Usuários"
3. Clique em "Adicionar Usuário"
4. Preencha nome, email e selecione "ativo"
5. Salve

### Criar uma Tarefa com Responsável
1. Clique em "✨ Criar Nova Tarefa"
2. Preencha título e descrição
3. **Selecione um usuário responsável no dropdown**
4. Defina prioridade e data de vencimento (opcionais)
5. Clique em "💾 Criar Tarefa"

### Visualizar Tarefas
- A página inicial mostra todas as tarefas em cards
- **Cada tarefa exibe o nome do usuário responsável**
- Clique na tarefa para ver detalhes completos (incluindo responsável com link)
- Use o filtro para visualizar por status

### Visualizar Usuários
1. Clique em "👥 Gerenciar Usuários" na listagem de tarefas
2. Veja a lista de usuários ativos
3. Clique em "Ver Detalhes" para ver o perfil
4. Veja todas as tarefas atribuídas ao usuário

### Editar Tarefa (Alterar Responsável)
1. Na listagem, clique em "Editar"
2. Altere o campo "Responsável" 
3. Pode deixar vazio para remover o responsável
4. Clique em "💾 Atualizar Tarefa"

### Atribuir Tarefa Existente
1. Clique em "Editar" na tarefa
2. No dropdown "Responsável", selecione um usuário
3. Salve a tarefa

## 🎨 Interface

A interface possui:
- Design moderno com gradients roxos
- Cards com animações suaves
- Badges de status e prioridade com cores distintas
- **Exibição clara do responsável em cada tarefa**
- **Links entre tarefas e usuários responsáveis**
- Responsivo para dispositivos móveis
- Ícones emoji para melhor visualização

## ⚙️ Configuração do Django

Apps registrados em `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'usuarios',  # NOVO!
    'tarefas',
]
```

URLs configuradas:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # NOVO!
    path('tarefas/', include('tarefas.urls')),
]
```

## 🔐 Admin Django

Gerenciar através do admin em http://127.0.0.1:8000/admin/:

### Usuários
- Ver lista de usuários
- Criar novos usuários
- Filtrar por status ativo/inativo
- Buscar por nome ou email
- Editar/deletar usuários

### Tarefas
- Ver lista de tarefas
- Filtro por status e conclusão
- Buscar por título e descrição
- **Ver responsável de cada tarefa**
- Editar/deletar tarefas

## 📱 Estrutura de Arquivos

```
usuarios/
├── models.py                    # Modelo Usuario
├── views.py                     # Views de usuários
├── urls.py                      # URLs de usuários
├── admin.py                     # Configuração admin
├── migrations/
│   └── 0001_initial.py         # Migração inicial
└── templates/usuarios/
    ├── listar.html             # Lista de usuários
    └── detalhe.html            # Detalhes do usuário

tarefas/
├── models.py                    # Modelo Tarefa (com ForeignKey)
├── views.py                     # Views de tarefas (atualizado)
├── urls.py                      # URLs de tarefas
├── admin.py                     # Configuração admin
├── migrations/
│   ├── 0001_initial.py
│   └── 0002_tarefa_usuario_responsavel.py  # Novo campo
└── templates/tarefas/
    ├── listar.html             # Lista (mostra responsável)
    ├── detalhe.html            # Detalhes (mostra responsável)
    ├── criar.html              # Formulário com responsável
    ├── atualizar.html          # Edição com responsável
    └── deletar.html            # Confirmação exclusão
```

## 🔗 Relacionamentos

```
Usuario (1) ──── (*) Tarefa
  - Um usuário pode ter múltiplas tarefas
  - Uma tarefa pode ter um usuário responsável ou nenhum
  - Ao deletar usuário, tarefas ficam sem responsável (SET_NULL)
```

## 💡 Funcionalidades Principais

✅ **Gestão de Usuários**
- Criar, visualizar, editar e deletar usuários
- Ativar/desativar usuários
- Ver todas as tarefas de um usuário

✅ **Atribuição de Tarefas**
- Atribuir tarefa ao criar
- Alterar responsável ao editar
- Remover responsável deixando vazio

✅ **Visualização Integrada**
- Tarefas mostram responsável em cards
- Usuários mostram suas tarefas atribuídas
- Links bidirecionais entre tarefas e usuários

✅ **Filtros e Buscas**
- Admin: filtrar usuários por status
- Admin: buscar por nome ou email
- Tarefas: filtro por status ainda disponível

## 🧪 Como Testar

### Via Interface Web
1. Criar 2-3 usuários no admin
2. Criar tarefas e atribuir a usuários
3. Visualizar na lista de tarefas
4. Clicar em usuário responsável para ir ao perfil
5. No perfil do usuário, ver suas tarefas

### Via Django Admin
1. Acessar http://127.0.0.1:8000/admin/
2. Criar usuários em "Usuários"
3. Criar tarefas em "Tarefas" (selecionar responsável)
4. Editar tarefas para mudar responsável

### Via Django Shell
```bash
python manage.py shell
```

```python
from usuarios.models import Usuario
from tarefas.models import Tarefa

# Criar usuário
usuario = Usuario.objects.create(nome="João", email="joao@email.com")

# Criar tarefa atribuída
tarefa = Tarefa.objects.create(
    titulo="Teste",
    usuario_responsavel=usuario
)

# Listar tarefas de um usuário
tarefas_usuario = usuario.tarefas.all()

# Listar tarefas sem responsável
sem_responsavel = Tarefa.objects.filter(usuario_responsavel__isnull=True)
```

## 📊 Detalhes de Implementação

### Campo ForeignKey
```python
usuario_responsavel = models.ForeignKey(
    Usuario,
    on_delete=models.SET_NULL,  # Tarefa fica sem responsável
    null=True,                   # Permite nulo
    blank=True,                  # Campo opcional no form
    related_name='tarefas'       # Acesso reverso: usuario.tarefas.all()
)
```

### Select Related
Na view de listagem, otimizado com:
```python
tarefas = Tarefa.objects.select_related('usuario_responsavel').all()
```
Evita múltiplas queries ao banco (N+1 problem)

## ⚠️ Casos Especiais

### Deletar Usuário
- Tarefas atribuídas ficam com `usuario_responsavel = null`
- Tarefas continuam existindo
- Appear como "Não atribuído" na interface

### Deletar Tarefa
- Remove apenas a tarefa
- Não afeta o usuário

### Desativar Usuário
- Usuário não aparece na seleção de responsável
- Tarefas já atribuídas mantêm referência
- Pode ser reativado depois

## 🔮 Próximas Evoluções

- [ ] Autenticação de usuários
- [ ] Tarefas por usuário logado
- [ ] Categorias/Etiquetas em tarefas
- [ ] Subtarefas
- [ ] Comentários em tarefas
- [ ] API REST com DRF
- [ ] Notificações por email
- [ ] Histórico de alterações
- [ ] Busca avançada por responsável
- [ ] Relatórios por usuário

---

**✅ Evoluído com relação usuário-tarefa!**

Última atualização: Abril 2026  
Status: ✨ PRONTO PARA USO
