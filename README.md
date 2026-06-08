# Lab Backend P2 — API de Catálogo de Jogos

API REST desenvolvida com Django 6 e Django REST Framework para gerenciar um catálogo de jogos, com banco de dados PostgreSQL.

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (incluso no Docker Desktop)

## Configuração do ambiente

Copie o arquivo de exemplo e preencha as variáveis:

```bash
cp .env.example .env
```

Edite o `.env` com seus valores:

```env
DJANGO_SECRET_KEY=sua-chave-secreta-aqui

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha

ALLOWED_HOSTS=*

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=senha-do-admin
```

> `POSTGRES_HOST` deve ser `postgres` (nome do serviço no Docker Compose).

## Rodando com Docker

```bash
docker compose up -d
```

O Docker irá:
1. Subir o container do PostgreSQL
2. Aguardar o banco estar pronto (healthcheck)
3. Executar as migrations automaticamente
4. Criar o superusuário com as credenciais do `.env`
5. Iniciar o servidor na porta `8000`

Acompanhe os logs com:

```bash
docker compose logs -f
```

## Endpoints da API

Base URL: `http://localhost:8000`

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/jogos/` | Lista todos os jogos |
| GET | `/api/jogos/anunciados` | Lista jogos anunciados |
| GET | `/api/jogos/pre-venda` | Lista jogos em pré-venda |
| GET | `/api/jogos/lancados` | Lista jogos lançados |

## Painel administrativo

Acesse `http://localhost:8000/admin/` com as credenciais definidas nas variáveis `DJANGO_SUPERUSER_*` do `.env`.

## Parando os containers

```bash
docker compose down
```

Para remover também os dados do banco:

```bash
docker compose down -v
```
