# Desafio DIO – Cenários Controlados para Estudo de Vulnerabilidades

Este repositório implementa um **ambiente mínimo e didático** para simular e documentar vulnerabilidades em aplicações web. Ele inclui:
- **API (FastAPI + Uvicorn)** com endpoints de exemplo para exploração e testes;
- **Frontend** estático com **Cytoscape.js** para visualizar graficamente os fluxos e nós do sistema;
- **Documentação STRIDE** com mapeamento de ameaças e controles;
- Estrutura preparada para **prints** na pasta `images/` e guia de execução.

## 🎯 Objetivos de Aprendizagem
- Aplicar conceitos de segurança em um ambiente prático;
- Documentar processos técnicos de forma clara e estruturada;
- Utilizar o **GitHub** para versionar e compartilhar a documentação técnica.

## 🧱 Arquitetura (Visão Geral)
```
frontend (Cytoscape)  →  API FastAPI  →  (futuro) Banco de Dados
```
O frontend consome a API e exibe um grafo de componentes/fluxos. A API inclui endpoints intencionalmente simples para facilitar a criação de **cenários controlados** (e.g., validação insuficiente, enumeração de recursos, etc.).

## 🚀 Como Executar (Backend)
```bash
# 1) Crie e ative um ambiente virtual (opcional)
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# 2) Instale dependências
pip install -r backend/requirements.txt

# 3) Rode a API (hot-reload)
uvicorn backend.main:app --reload
# Servirá em http://127.0.0.1:8000
# Docs interativas: http://127.0.0.1:8000/docs
```

## 🌐 Como Usar (Frontend)
Abra o arquivo `frontend/index.html` diretamente no navegador **após** subir a API.  
O grafo inicial é montado localmente e o botão **"Carregar Vulnerabilidades"** consulta `GET /vulns` na API (CORS liberado).

## 🧪 Endpoints de Exemplo
- `GET /` — status básico da API
- `GET /vulns` — lista simulada de vulnerabilidades
- `POST /scan` — simula uma varredura (entrada controlada)
- `GET /echo?text=` — **(intencionalmente simplista)** útil para discutir *reflected input* e validação

> **Atenção:** o objetivo é **aprender**. Não exponha esse ambiente em produção.

## 🔒 Metodologia de Ameaças
A documentação do método está em `threats/metodologia.md`, com foco em **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) e sugestões de controles.

## 🖼 Evidências
Adicione suas capturas de tela em `images/` e referencie-as no README.

## 📦 Estrutura
```
desafio-seguranca-app/
├── README.md
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── threats/
│   └── metodologia.md
└── images/
    └── .gitkeep
```

## 🧭 Roteiro sugerido para o desafio
1. Executar a API e validar endpoints via `/docs` (Swagger);
2. Abrir o frontend e visualizar o grafo;
3. Simular cenários: entradas malformadas, parâmetros inesperados, rate limit inexistente, etc.;
4. Documentar casos de teste e evidências (prints);
5. Criar o repositório público e enviar o link na plataforma.

## 📜 Licença
MIT – uso livre para fins educacionais.
