import json
from .parser import parseArgs
from .core import (
    loadCsv,
    totaPorProduto,
    filtrarPorData,
    totaVendasGeral,
    totaItensVendidos,
    produtoMaisVendido,
    totalSKU
)


def main():
    args = parseArgs()
    dados = loadCsv(args.csv_path)
    dados = filtrarPorData(dados, args.start, args.end)

    match args.calc:
        case "total_produto":
            totais = totaPorProduto(dados)
            if args.format == "json":
                print(json.dumps(totais, indent=2, ensure_ascii=False))
            else:
                print("\n📦 Total por produto:")
                for produto, total in totais.items():
                    print(f"  {produto:<20} R$ {total:.2f}")

        case "total_geral":
            total = totaVendasGeral(dados)
            if args.format == "json":
                print(json.dumps({"total_geral": total},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n💰 Valor total de vendas: R$ {total:.2f}")

        case "itens":
            itens = totaItensVendidos(dados)
            if args.format == "json":
                print(json.dumps({"itens_vendidos": itens},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n📦 Total de itens vendidos: {itens}")

        case "sku":
            sku = totalSKU(dados)
            if args.format == "json":
                print(json.dumps({"skus_diferentes": sku},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n🔢 Total de produtos distintos (SKU): {sku}")

        case "mais_vendido":
            mv = produtoMaisVendido(dados)
            if args.format == "json":
                print(json.dumps({"mais_vendido": mv},
                      indent=2, ensure_ascii=False))
            else:
                for produto, valor in mv.items():
                    print(
                        f"\n🏆 Produto mais vendido: {produto} (R$ {valor:.2f})")

        case "tudo":
            # total por produto
            totais = totaPorProduto(dados)
            if args.format == "json":
                print(json.dumps({"total_por_produto": totais},
                      indent=2, ensure_ascii=False))
            else:
                print("\n📦 Total por produto:")
                for produto, total in totais.items():
                    print(f"  {produto:<20} R$ {total:.2f}")

            # total geral
            total = totaVendasGeral(dados)
            if args.format == "json":
                print(json.dumps({"total_geral": total},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n💰 Valor total de vendas: R$ {total:.2f}")

            # itens vendidos
            itens = totaItensVendidos(dados)
            if args.format == "json":
                print(json.dumps({"itens_vendidos": itens},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n📦 Total de itens vendidos: {itens}")

            # SKUs
            sku = totalSKU(dados)
            if args.format == "json":
                print(json.dumps({"skus_diferentes": sku},
                      indent=2, ensure_ascii=False))
            else:
                print(f"\n🔢 Total de produtos distintos (SKU): {sku}")

            # mais vendido
            mv = produtoMaisVendido(dados)
            if args.format == "json":
                print(json.dumps({"mais_vendido": mv},
                      indent=2, ensure_ascii=False))
            else:
                for produto, valor in mv.items():
                    print(
                        f"\n🏆 Produto mais vendido: {produto} (R$ {valor:.2f})")

        case _:
            print("❌ Cálculo inválido.")


if __name__ == "__main__":
    main()
