# ⚽ Django Football Teams Hub

Uma aplicação web desenvolvida em **Django** para o gerenciamento centralizado de clubes de futebol de todo o mundo. O projeto oferece um ciclo completo de CRUD (Create, Read, Update, Delete) com uma interface moderna e responsiva.

> Projeto desenvolvido como atividade prática de curso, com foco em boas práticas de desenvolvimento Django.

---

## ✨ Funcionalidades

- **Dashboard Principal:** Interface de boas-vindas com contador dinâmico de registros.
- **CRUD Completo:**
  - 📋 **Listagem:** Visualização em tabela com suporte a hover e listras.
  - ➕ **Cadastro:** Inclusão de novos times com validação automática via ModelForm.
  - ✏️ **Edição:** Atualização de dados reaproveitando o mesmo formulário do cadastro.
  - 🗑️ **Exclusão Segura:** Fluxo de confirmação para evitar deleções acidentais.
- **Admin Customizado:** Interface administrativa configurada com `list_display`, `list_filter` e `search_fields`.
- **Arquitetura DRY:** Herança de templates (`base.html`) para evitar repetição de código.
- **Formulários Inteligentes:** `ModelForm` com aplicação automática de classes Bootstrap via `__init__`.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.14 | Linguagem base |
| Django 6.0 | Framework web |
| Bootstrap 5 | Layout e UI responsiva |
| SQLite | Banco de dados local |

---

## 📁 Estrutura do Projeto

```
django-football-teams-hub/
│
├── futebol_project/          ← Configurações globais do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── times/                    ← Aplicação principal
│   ├── migrations/           ← Migrações do banco de dados
│   ├── templates/
│   │   └── times/
│   │       ├── base.html             ← Template base (Bootstrap)
│   │       ├── home.html             ← Dashboard inicial
│   │       ├── listar_times.html     ← Listagem de times
│   │       ├── form_time.html        ← Formulário (criar e editar)
│   │       └── confirm_delete.html   ← Confirmação de exclusão
│   ├── admin.py              ← Painel admin customizado
│   ├── apps.py
│   ├── forms.py              ← ModelForm com Bootstrap automático
│   ├── models.py             ← Model Time
│   ├── urls.py               ← Rotas da aplicação
│   └── views.py              ← Views do CRUD
│
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/CaioGomes26/django-football-teams-hub.git
cd django-football-teams-hub
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações
```bash
python manage.py migrate
```

### 5. Crie o superusuário
```bash
python manage.py createsuperuser
```

### 6. Rode o servidor
```bash
python manage.py runserver
```

---

## 🔗 Mapa de Rotas

| Rota | Descrição |
| :--- | :--- |
| `/` | Dashboard / Home |
| `/times/` | Listagem geral |
| `/times/cadastrar/` | Formulário de cadastro |
| `/times/editar/<id>/` | Edição de registro |
| `/times/deletar/<id>/` | Confirmação de exclusão |
| `/admin/` | Painel do administrador |

---

## 📋 Model Time

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | CharField | Nome do clube |
| `ano_fundacao` | PositiveIntegerField | Ano de fundação |
| `pais` | CharField | País do clube |
| `estado` | CharField | Estado/Região |
| `cidade` | CharField | Cidade sede |

---

## Autor
- Caio Gomes de Oliveira
