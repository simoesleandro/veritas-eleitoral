from unittest.mock import patch
from veritas.agentes.verificador import verificar_claim
from core.modelos import ClaimExtraida, Evidencia, ResultadoVerificacao


def test_verificar_claim_retorna_resultado_verificacao():
    claim = ClaimExtraida(texto="zero crescimento", checavel=True, confianca=0.9)
    evidencias = [
        Evidencia(fonte="IBGE", trecho="cresceu 8.2%", url="u1"),
        Evidencia(fonte="Estadao Verifica", trecho="mesma checagem anterior: falso", url="u2"),
    ]
    fake_result = ResultadoVerificacao(
        veredito="falso", evidencias=evidencias, fontes_independentes=2,
        confianca=0.9, justificativa="IBGE aponta 8.2%", contraposicao_sugerida="cresceu 8.2%"
    )
    with patch("veritas.agentes.verificador.gerar_resposta", return_value=fake_result):
        result = verificar_claim(claim, evidencias)
    assert result.veredito == "falso"


def test_verificar_claim_demo_desemprego_zero_sem_llm():
    claim = ClaimExtraida(
        texto="o desemprego no Brasil caiu para zero em 2024",
        checavel=True,
        confianca=0.98,
    )
    evidencias = [
        Evidencia(fonte="IBGE / PNAD Continua", trecho="ha populacao desocupada", url="u1"),
        Evidencia(fonte="Agencia Brasil", trecho="queda nao significa zero", url="u2"),
    ]

    result = verificar_claim(claim, evidencias)

    assert result.veredito == "falso"
    assert result.fontes_independentes == 2
