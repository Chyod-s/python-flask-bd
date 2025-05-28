## Endpoints

---

### GET `/`
**Descrição:**  
Exibe a interface do Swagger UI para documentação e testes da API.


### POST `/api/register`
**Descrição:**
Registra um novo usuário.

```json
{
  "user_name": "klay",
  "email": "hix_x@hotmail.com",
  "password": "123",
  "confirm_password": "123",
  "name": "Klayton Dias"
}
```

```json
Status: 201 Created Size: 511 Bytes Time: 293 ms
```

### Resposta de Sucesso:

**Código:** 201 Created

**Corpo:**
```json
{
  "status": "success",
  "message": "Usuário criado com sucesso!",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiaWF0IjoxNzQ4NDYyOTEyLCJleHAiOjE3NDg0NjY1MTIsImp0aSI6Ijc3ZGM5ODA0LWZlNGItNDFlNy04NDM1LTEzNTc2NWE2ZGU2MyIsInR5cGUiOiJhY2Nlc3MiLCJuYmYiOjE3NDg0NjI5MTIsImNzcmYiOiI5ZDJmNGRhMS0zNDI1LTRlOGMtYmM5MS0wMWIzOWMzMjc1OTQifQ.qRYyzjUShkdRmmwQc3F2whUhxGp9dx7zeSUDLyNdYEQ",
    "csrf_token": "9d2f4da1-3425-4e8c-bc91-01b39c327594",
    "user_id": 1
  }
}
```

### POST `/api/login`
**Descrição:**
Autentica um usuário e retorna um token JWT, csrf_token, user_name.

**Body (JSON):**
```json
{
  "user_name_email": "klay",
  "password": "123"
}
```
```json
Status: 200 OK Size: 0 Bytes Time: 156 ms
```
### Resposta de Sucesso:

**Código:** 200 OK

**Corpo:**

```json
{
  "data": {
    "csrf_token": "dd3fcacb-4f5f-4824-860d-628f3074e5c6",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiaWF0IjoxNzQ4NDYzMTY0LCJleHAiOjE3NDg0NjY3NjQsImp0aSI6ImU2YTY0ZjhhLWU5M2QtNDY4Ni04ZGI4LTAxMDY3YmQ2MmVkZiIsInR5cGUiOiJhY2Nlc3MiLCJuYmYiOjE3NDg0NjMxNjQsImNzcmYiOiJkZDNmY2FjYi00ZjVmLTQ4MjQtODYwZC02MjhmMzA3NGU1YzYifQ.MwmQ376B4ZV9W7WL98_evVLXErEplCkfrILJOp-e-RM",
    "user_name": "Klayton Dias"
  },
  "message": "Usuário autenticado com sucesso!",
  "status": "success"
}
```



## Autenticação
Algumas rotas exigem autenticação JWT. Envie o token no cabeçalho `Authorization`:

```makefile
Authorization: Bearer JWT_TOKEN
```
## Erros Comuns
- 401 Unauthorized: Token inválido ou ausente

- 400 Bad Request: Campos obrigatórios ausentes ou inválidos

- 500 Internal Server Error: Erro interno da aplicação

## Visão geral de tempo de resposta Jacob Nielsen, Google Web Vitals, Experiências e benchmarks em APIs REST

| Tempo de resposta | Classificação Geral              |
|-------------------|----------------------------------|
| 0–100ms           | Excelente (quase instantâneo)    |
| 100–300ms         | Muito bom / aceitável            |
| 300–500ms         | Bom, mas pode melhorar           |
| 500ms–1s          | Limite tolerável                 |
| > 1s              | Pode causar frustração           |