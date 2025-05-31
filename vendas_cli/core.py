import csv
import logging
from datetime import datetime
from typing import List, Dict, Optional


def loadCsv(path: str) -> List[Dict[str, str]]:
    try:
        with open(path, mode="r", encoding="latin1") as f:
            reader = csv.DictReader(f)
            dados = list(reader)
            return dados
    except FileNotFoundError:
        logging.error(f"❌ Arquivo não encontrado: {path}")
        return []
    except Exception as e:
        logging.error(f"❌ Erro ao ler CSV: {e}")
        return []


def filtrarPorData(dados: List[Dict[str, str]],
                   start: Optional[str],
                   end: Optional[str]) -> List[Dict[str, str]]:
    if not start and not end:
        return dados

    dados_filtrados = []
    for linha in dados:
        try:
            data_venda = datetime.strptime(linha["data_venda"], "%Y-%m-%d")
            if start:
                data_inicio = datetime.strptime(start, "%Y-%m-%d")
                if data_venda < data_inicio:
                    continue
            if end:
                data_fim = datetime.strptime(end, "%Y-%m-%d")
                if data_venda > data_fim:
                    continue
            dados_filtrados.append(linha)
        except Exception as e:
            logging.warning(f"Erro ao filtrar data: {linha} | {e}")
            continue

    return dados_filtrados


def totaPorProduto(dados: List[Dict[str, str]]) -> Dict[str, float]:
    totais: Dict[str, float] = {}

    for item in dados:
        try:
            produto = item["produto"]
            quantidade = int(item["quantidade"])
            preco = float(item["preco_unitario"])
            total_venda = quantidade * preco
        except Exception as e:
            logging.warning(
                f"⚠️ Erro ao processar linha: {item} | Erro: {e}")
            continue

        totais[produto] = totais.get(produto, 0) + total_venda

    return totais


def totaVendasGeral(dados: List[Dict[str, str]]) -> Dict[str, float]:
    total = 0.0

    for item in dados:

        quantidade = int(item['quantidade'])
        preco = float(item["preco_unitario"])
        total += quantidade * preco

    return total


def totaItensVendidos(dados: List[Dict[str, str]]) -> Dict[str, float]:
    totaItensVendidos = 0
    for item in dados:
        quantidade = int(item["quantidade"])

        totaItensVendidos += quantidade

    return totaItensVendidos


def produtoMaisVendido(dados: List[Dict[str, str]]) -> Dict[str, float]:
    totais: Dict[str, float] = {}

    for linha in dados:
        try:
            produto = linha["produto"]
            quantidade = int(linha["quantidade"])
            preco = float(linha["preco_unitario"])
            total_venda = quantidade * preco
            totais[produto] = totais.get(produto, 0) + total_venda
        except Exception as e:
            logging.warning(f"⚠️ Erro na linha: {linha} | Erro: {e}")
            continue

    if not totais:
        return {}

    mais_vendido = max(totais.items(), key=lambda item: item[1])
    return {mais_vendido[0]: mais_vendido[1]}


def totalSKU(dados: List[Dict[str, str]]) -> Dict[str, float]:
    skus = set()
    for item in dados:
        produto = item.get("produto")
        if produto:
            skus.add(produto)

    return len(skus)
