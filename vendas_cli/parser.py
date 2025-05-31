import argparse
from argparse import Namespace


def parseArgs() -> Namespace:
    parser = argparse.ArgumentParser(
        prog='MiranteDash',
        description="Gerador de Relatório de Vendas Mirante")

    parser.add_argument("csv_path", type=str,
                        help="Argunmento para Caminho do CSV")
    parser.add_argument("--start", type=str,
                        help="Data inicial (YYYY-MM-DD)", default=None)
    parser.add_argument("--end", type=str,
                        help="Data final (YYYY-MM-DD)", default=None)
    parser.add_argument(
        "--calc",
        choices=["total_produto", "total_geral",
                 "itens", "sku", "mais_vendido", "tudo"],
        default="tudo",
        help="Tipo de cálculo a ser feito! Coloquei o ""tudo"" como padrão"
    )
    parser.add_argument(
        "--format", choices=["text", "json"], default="text", help="Tipo de Saída")

    parser.add_argument(
        "--engine",
        choices=["builtin", "pandas"],
        default="builtin",
        help="Engine de processamento: builtin (padrão) ou pandas"
    )
    return parser.parse_args()
