# Veritas Eleitoral

MVP de fact-checking eleitoral assistido por IA. O projeto recebe uma afirmacao politica, extrai claims verificaveis, pesquisa evidencias em fontes publicas, classifica o veredito e registra um dossie de checagem.

Este repositorio nasceu como uma extracao enxuta do EleitorAI: a ideia original era ampla demais para ficar apresentavel como projeto de portfolio. Aqui o foco e um produto menor, testavel e facil de explicar para recrutadores.

## Por que importa

Campanhas, jornalistas locais e equipes civicas precisam responder rapidamente a informacoes falsas ou enganosas. O Veritas Eleitoral organiza esse fluxo em uma aplicacao web simples: entrada manual da claim, processamento em fila, analise por IA, evidencias auditaveis e historico de checagens.

## Funcionalidades

- Dashboard com KPIs de mencoes, checagens, alertas e fila de jobs.
- Formulario para submeter claims eleitorais.
- Pipeline Veritas com extracao de afirmacoes, pesquisa de evidencias e classificacao de veredito.
- Base SQLite com extensao vetorial `sqlite-vec` para apoio a RAG.
- Worker separado para processar checagens em background.
- Alertas para claims falsas ou enganosas.
- Download do dossie em Markdown.
- Testes automatizados para core, app e ferramentas Veritas.

## Stack

- Python 3.11+
- Flask
- SQLite + sqlite-vec
- Pydantic
- Google Gemini API
- LangGraph
- APScheduler
- Pytest

## Como rodar localmente

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edite `.env` e preencha:

```env
GEMINI_API_KEY=sua_chave
SECRET_KEY=uma_chave_local
DB_PATH=data/veritas_eleitoral.db
```

Inicialize o banco:

```powershell
python -c "from core.db import init_db; init_db()"
```

Rode a aplicacao:

```powershell
flask --app app run --debug
```

Em outro terminal, processe a fila:

```powershell
python -m worker --once
```

## Testes

```powershell
pytest tests/core tests/veritas -q
```

## Competencias demonstradas

- Recorte de escopo e transformacao de uma ideia grande em MVP.
- Arquitetura Flask com separacao entre web, core, pipeline de IA e worker.
- Modelagem relacional para checagens, evidencias, alertas e fila.
- Uso de IA generativa com validacao estruturada via Pydantic.
- Testes de unidade e integracao em pontos criticos.
- Documentacao orientada a portfolio e manutencao futura.

## Roadmap

- Adicionar seed inicial para fontes publicas confiaveis.
- Adicionar exportacao de dossies em PDF.
- Criar tela de detalhe com rastreabilidade completa das evidencias.
- Adicionar exemplos reais de claims eleitorais para demonstracao.
- Publicar deploy demonstrativo com dados ficticios.

## Status

MVP em consolidacao. O objetivo atual e deixar o projeto pequeno, funcional e apresentavel antes de adicionar novas fontes ou automacoes.
