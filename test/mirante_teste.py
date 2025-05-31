import pytest
from vendas_cli.core import (
    totaPorProduto,
    totaVendasGeral,
    totaItensVendidos,
    produtoMaisVendido,
    totalSKU,
    filtrarPorData
)

# Dados simulados
dados = [
    {"produto": "Camiseta", "quantidade": "2",
        "preco_unitario": "50.0", "data_venda": "2024-01-01"},
    {"produto": "Calça", "quantidade": "1",
        "preco_unitario": "100.0", "data_venda": "2024-01-02"},
    {"produto": "Camiseta", "quantidade": "1",
        "preco_unitario": "50.0", "data_venda": "2024-01-03"},
]


def test_total_por_produto():
    resultado = totaPorProduto(dados)
    assert resultado["Camiseta"] == 150.0
    assert resultado["Calça"] == 100.0


def test_total_geral():
    resultado = totaVendasGeral(dados)
    assert resultado == 250.0


def test_total_itens():
    resultado = totaItensVendidos(dados)
    assert resultado == 4


def test_produto_mais_vendido():
    resultado = produtoMaisVendido(dados)
    assert list(resultado.keys())[0] == "Camiseta"
    assert list(resultado.values())[0] == 150.0


def test_total_skus():
    resultado = totalSKU(dados)
    assert resultado == 2


def test_filtrar_por_data():
    resultado = filtrarPorData(dados, "2024-01-02", "2024-01-03")
    assert len(resultado) == 2
    assert resultado[0]["produto"] == "Calça"
    assert resultado[1]["produto"] == "Camiseta"
