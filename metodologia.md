# Metodologia de Ameaças – STRIDE (Aplicada ao Projeto)

Este documento aplica **STRIDE** ao nosso ambiente didático para apoiar a criação de **cenários controlados**.

## Escopo do Modelo
- **Ativos**: API (FastAPI), Frontend (Cytoscape), dados de requisição/resposta
- **Atores**: Usuário legítimo, Atacante externo (não autenticado)
- **Fluxos**: Frontend → API (`/vulns`, `/echo`, `/scan`)

## STRIDE
### S – Spoofing (Falsificação de Identidade)
- **Risco**: ausência de autenticação pode permitir simulações de identidade.
- **Cenário Controlado**: chamadas a `/scan` sem autenticação.
- **Mitigações**: autenticação (JWT/OAuth2), validação de origem, logs.

### T – Tampering (Adulteração)
- **Risco**: manipulação de parâmetros (`/echo`, body de `/scan`).
- **Cenário Controlado**: envio de cargas com caracteres especiais e scripts.
- **Mitigações**: saneamento/validação, tipos fortes (Pydantic), WAF, schema strict.

### R – Repudiation (Repúdio)
- **Risco**: falta de trilhas de auditoria torna difícil atribuir ações.
- **Cenário**: uso de `/scan` sem correlação de usuário/tempo/IP.
- **Mitigações**: logs estruturados, correlação de requisições, retenção definida.

### I – Information Disclosure (Divulgação)
- **Risco**: respostas verbosas podem vazar detalhes do sistema.
- **Cenário**: mensagens de erro detalhadas em exceções.
- **Mitigações**: mensagens genéricas, níveis de log, revisão de respostas.

### D – Denial of Service (DoS)
- **Risco**: endpoints sem rate limit podem ser abusados.
- **Cenário**: loop de chamadas a `/scan`.
- **Mitigações**: rate limiting, timeouts, filas, circuit breaker.

### E – Elevation of Privilege (Elevação de Privilégio)
- **Risco**: endpoints sem autorização podem permitir ações indevidas.
- **Cenário**: alterar intensidade da varredura para “profunda” sem permissão.
- **Mitigações**: RBAC/ABAC, checagem de escopos, segmentação.

## Mapa Simplificado (para o Frontend)
- **Nós**: `frontend`, `api`, `db` (futuro)
- **Arestas**: `frontend→api`, `api→db`
- **Pontos de controle**: validação de entrada, autenticação, observabilidade.

## Evidências e Passos de Teste
1. Suba a API (`uvicorn backend.main:app --reload`).
2. Acesse `/docs` e teste `GET /echo?text=<payload>`.
3. Registre prints (HTTP 200, payload refletido) em `images/`.
4. Discuta riscos e mitigações neste arquivo.
