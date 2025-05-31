## Instalação

Clone o repositório e instale com:

```bash

git clone https://github.com/seuusuario/vendas-cli.git
cd vendas-cli
pip install .

vendas-cli data/vendasexemplo-python.csv --calc tudo --format text

Parâmetros disponíveis:
csv_path	Caminho para o arquivo CSV de vendas
--calc	Cálculo: total_produto, total_geral, itens, sku, mais_vendido, tudo
--start	Data inicial do filtro opcional "YYYY-MM-DD"
--end	Data final do filtro opcional "YYYY-MM-DD"
--format	text "Tabela" ou json "Json"

vendas-cli data/vendasexemplo-python.csv  --format json  "Vem por padrão Tudo"

vendas-cli data/vendasexemplo-python.csv --calc total_produto --format text

vendas-cli data/vendasexemplo-python.csv --calc total_geral --format json

vendas-cli data/vendasexemplo-python.csv --calc tudo --start 2024-01-01 --end 2024-03-31


#TEST com Pytest. Na pasta Raiz, MIRANTE, usar o comando! 

 pytest test/mirante_teste.py
