# Como Criar uma Nova Rota na API 

## Estrutura do Projeto para criação de novo endpoint

```psql
src/
├── domain/
│   └── models/
│       └── users_model.ts                     ← Define a modelo `User`
│
├── usecases/
│   └── users/
│       └── login_user_use_case.ts       ← Lógica para criar a tarefa
│
├── http/
│   ├── controllers/
│   |   └── user_controller/           ← Controller que chama o usecase
│   |       
│   ├── routes/
|         └── back_end_routes.ts     ← definição das rotas back end           
│
├── main.py ← inicialização servidor     
```

## 1. Criando novo modelo no banco de dados

**Arquivo:** `./domain/models/user_model.py`


```python
from sqlalchemy import Column, Integer, String
from src.infrastructure.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)

```