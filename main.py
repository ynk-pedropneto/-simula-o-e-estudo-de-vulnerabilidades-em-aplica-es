from fastapi import FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Desafio DIO - API de Segurança", version="0.1.0")

# CORS liberado para facilitar testes locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    alvo: str
    intensidade: Optional[str] = "rapida"  # rapida | padrao | profunda

class Vulnerabilidade(BaseModel):
    id: int
    titulo: str
    descricao: str
    categoria: str
    severidade: str

VULNS_DB = [
    Vulnerabilidade(
        id=1,
        titulo="Validação insuficiente de entrada",
        descricao="Endpoint /echo reflete entradas sem saneamento adequado (cenário controlado).",        categoria="Input Validation",
        severidade="Alta",
    ),
    Vulnerabilidade(
        id=2,
        titulo="Enumeração previsível de recursos",
        descricao="IDs sequenciais permitem inferência de registros (exemplo teórico).",        categoria="IDOR",
        severidade="Média",
    ),
]

@app.get("/")
def root():
    return {"message": "API funcionando! Bem-vindo ao desafio de segurança DIO."}

@app.get("/vulns", response_model=List[Vulnerabilidade])
def listar_vulns():
    return VULNS_DB

@app.post("/scan")
def scan(req: ScanRequest):
    """Simula uma varredura no alvo informado."""
    resumo = {
        "alvo": req.alvo,
        "intensidade": req.intensidade,
        "encontradas": len(VULNS_DB),
        "observacoes": "Varredura simulada com base em regras estáticas.",
    }
    return {"status": "ok", "resultado": resumo}

@app.get("/echo")
def echo(text: str = Query("", description="Texto a ser refletido (uso didático)", max_length=200)):
    # intencionalmente simples para discussão didática
    return {"echo": text}
