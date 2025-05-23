# Template

Este projeto é uma API com frontend integrado. Desenvolvido com **Python**, **Flask**, **SQLAlchemy**, **JWT**, **Tailwind CSS** com **Alembic** para versionamento e arquitetura baseada em **Clean Architecture**.

---

## Tecnologias Utilizadas

- **Backend:** Python, Flask, SQLAlchemy, Alembic
- **Frontend:** Jinja2, Tailwind CSS, JavaScript
- **Autenticação:** JWT
- **Banco de Dados:** SQLite (desenvolvimento), com suporte para outros via SQLAlchemy
- **Task Scheduler:** Agendador customizado com execução via scripts
- **Containerização:** Docker + Docker Compose
- **Test:** Pytest

---

## Autenticação

O projeto utiliza **JWT** para autenticação de usuários. As rotas protegidas exigem envio de token no cabeçalho `Authorization`.

---
Configuração e Execução (Docker)

### Pré-requisitos
- [Docker `download`](https://www.docker.com/get-started/)

### Instalação manual

1 - Suba os containers com build forçado:
```bash
docker-compose up -d --build
```
2 - Acesse a aplicação:
```bash
http://localhost:5055
```
---

Configuração e Execução (Desenvolvimento)

### Pré-requisitos

- Python 3.10+
- Docker & Docker Compose (opcional)
- Node.js (para Tailwind)

### Instalação manual

```bash
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate # no linux  
.venv\Scripts\Activate.ps1 # no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
alembic upgrade head

# Inicie a aplicação
python src/api_main/main.py # api principal
python src/api_main/main.py # api mockada
```


Também organizei a estrutura pensando em facilitar os testes e a integração com outros ambientes. Usei pytest nos testes e deixei o projeto pronto pra rodar com Docker, o que ajuda na instalação e evita problemas com dependências.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
