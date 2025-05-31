
import pandas as pd


def executar_relatorio(args):
    df = pd.read_csv(args.csv_path, encoding="latin1")

    df["quantidade"] = pd.to_numeric(
        df["quantidade"], errors="coerce").fillna(0)
    df["preco_unitario"] = pd.to_numeric(
        df["preco_unitario"], errors="coerce").fillna(0)
    df["total"] = df["quantidade"] * df["preco_unitario"]

    if args.start and args.end:
        df = df[(df["data_venda"] >= args.start)
                & (df["data_venda"] <= args.end)]

    match args.calc:
        case "total_geral":
            print(df["total"].sum())
        case "total_produto":
            print(df.groupby("produto")["total"].sum())
        case "itens":
            print(df["quantidade"].sum())
        case "sku":
            print(df["produto"].nunique())
        case "mais_vendido":
            print(df.groupby("produto")["total"].sum(
            ).sort_values(ascending=False).head(1))
        case "tudo":
            print("📦 Total por produto:")
            print(df.groupby("produto")["total"].sum(), end="\n\n")

            print("💰 Total geral:")
            print(df["total"].sum(), end="\n\n")

            print("📦 Total de itens vendidos:")
            print(df["quantidade"].sum(), end="\n\n")

            print("🔢 Total de SKUs:")
            print(df["produto"].nunique(), end="\n\n")

            print("🏆 Produto mais vendido:")
            print(df.groupby("produto")["total"].sum(
            ).sort_values(ascending=False).head(1))
        case _:
            print("❌ Cálculo inválido.")
