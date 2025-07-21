from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate, add_pagination
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List

from database import SessionLocal, engine, Base
from models import Atleta
from schemas import AtletaCreate, AtletaResponse

app = FastAPI(title="Workout API")

# Liberação para CORS (opcional, bom para testes no navegador)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Dependência para pegar a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/atletas", response_model=AtletaResponse)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo = Atleta(**atleta.dict())
    try:
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

@app.get("/atletas", response_model=Page[AtletaResponse])
def listar_atletas(
    nome: Optional[str] = None,
    cpf: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    atletas = query.all()
    return paginate(atletas)

add_pagination(app)
