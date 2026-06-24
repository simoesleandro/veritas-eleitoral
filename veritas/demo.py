from core.modelos import ClaimExtraida, Evidencia, ResultadoVerificacao

_DESEMPREGO_ZERO_TOKENS = ("desemprego", "zero", "2024")


def _normalizar(texto: str) -> str:
    return " ".join(texto.lower().split())


def is_demo_desemprego_zero(texto: str) -> bool:
    normalizado = _normalizar(texto)
    return all(token in normalizado for token in _DESEMPREGO_ZERO_TOKENS)


def extrair_claims_demo(texto: str) -> list[ClaimExtraida]:
    if not is_demo_desemprego_zero(texto):
        return []
    return [
        ClaimExtraida(
            texto="o desemprego no Brasil caiu para zero em 2024",
            sujeito="desemprego no Brasil",
            predicado="caiu para zero em 2024",
            checavel=True,
            confianca=0.98,
        )
    ]


def evidencias_demo(claim: ClaimExtraida) -> list[Evidencia]:
    if not is_demo_desemprego_zero(claim.texto):
        return []
    return [
        Evidencia(
            fonte="IBGE / PNAD Continua",
            trecho=(
                "A PNAD Continua mede a taxa de desocupacao no Brasil e seus resultados "
                "recentes mostram existencia de populacao desocupada, nao desemprego zero."
            ),
            url="https://www.ibge.gov.br/estatisticas/sociais/trabalho.html",
        ),
        Evidencia(
            fonte="Agencia Brasil",
            trecho=(
                "Reportagens economicas sobre 2024 registram queda na taxa de desemprego, "
                "mas nao indicam eliminacao total do desemprego no pais."
            ),
            url="https://agenciabrasil.ebc.com.br/economia",
        ),
    ]


def verificacao_demo(claim: ClaimExtraida, evidencias: list[Evidencia]) -> ResultadoVerificacao | None:
    if not is_demo_desemprego_zero(claim.texto) or len(evidencias) < 2:
        return None
    return ResultadoVerificacao(
        veredito="falso",
        evidencias=evidencias,
        fontes_independentes=2,
        confianca=0.92,
        justificativa=(
            "A afirmacao diz que o desemprego caiu para zero em 2024. As evidencias "
            "indicam queda do desemprego, mas tambem mostram que ainda havia populacao "
            "desocupada. Portanto, a queda para zero e contradita pelas fontes."
        ),
        contraposicao_sugerida=(
            "O desemprego pode ter caido, mas nao chegou a zero. Dados publicos de "
            "trabalho ainda registram pessoas desocupadas no Brasil."
        ),
    )
