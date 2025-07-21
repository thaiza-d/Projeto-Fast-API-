# Workout API

Este é um projeto desenvolvido como parte do curso da DIO (Digital Innovation One), com o objetivo de aplicar os conhecimentos em FastAPI, SQLAlchemy e versionamento de código com Git.

## ✅ Funcionalidades Implementadas

- ✅ Cadastro de atletas com os campos: nome, CPF, centro de treinamento e categoria
- ✅ Filtro por `nome` e `cpf` nos endpoints de listagem
- ✅ Resposta customizada no endpoint de listagem com apenas: nome, centro de treinamento e categoria
- ✅ Tratamento de erro para CPF duplicado com código 303 e mensagem clara
- ✅ Paginação implementada com a biblioteca `fastapi-pagination`

## 📦 Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite (banco de dados local)
- Pydantic
- FastAPI Pagination
- Uvicorn (servidor ASGI)

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/workout_api_custom.git
cd workout_api_custom
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor local
```bash
uvicorn main:app --reload
```

### 5. Acesse a documentação interativa
Acesse no navegador:
```
http://127.0.0.1:8000/docs
```

---

## 🔎 Exemplos de Uso

### ✅ Cadastro de atleta
```json
POST /atletas
{
  "nome": "João Silva",
  "cpf": "12345678900",
  "centro_treinamento": "CT Rio",
  "categoria": "Profissional"
}
```

### ⚠️ Erro de CPF duplicado
Se tentar cadastrar o mesmo CPF:
```json
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678900"
}
```

### 🔍 Filtro por nome e CPF
```
GET /atletas?nome=João&cpf=12345678900
```

### 📄 Resposta customizada
```json
{
  "items": [
    {
      "nome": "João Silva",
      "centro_treinamento": "CT Rio",
      "categoria": "Profissional"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50
}
```

---

## 🧾 Certificação

Este projeto foi entregue como requisito para obtenção de certificado na plataforma DIO.

---

## 👩‍💻 Desenvolvido por

Thaiza Dantas ✨
