from pathlib import Path

from pydantic import BaseModel

from core.llm import gerar_resposta
from core.modelos import ClaimExtraida
from veritas.demo import extrair_claims_demo

_PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "extrator.txt"


class _ListaClaims(BaseModel):
    claims: list[ClaimExtraida]


def extrair_claims(texto: str, apenas_checaveis: bool = False) -> list[ClaimExtraida]:
    claims_demo = extrair_claims_demo(texto)
    if claims_demo:
        return [c for c in claims_demo if c.checavel] if apenas_checaveis else claims_demo

    prompt_sistema = _PROMPT_PATH.read_text(encoding="utf-8")
    prompt = f"{prompt_sistema}\n\nTexto para analisar:\n{texto}"
    resposta = gerar_resposta(prompt, response_schema=_ListaClaims)
    claims = resposta.claims
    if apenas_checaveis:
        claims = [c for c in claims if c.checavel]
    return claims
