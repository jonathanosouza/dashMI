# 🛒 vendas-cli

**vendas-cli** é uma ferramenta de linha de comando para geração de relatórios de vendas.  
Ela permite calcular totais por produto, totais gerais, quantidade de SKUs, produto mais vendido e muito mais — tudo via terminal e com suporte a filtros por data e saída em formato texto ou JSON.

---

## 🚀 Instalação

Clone o repositório e instale com:

```bash
git clone https://github.com/seuusuario/vendas-cli.git
cd vendas-cli
pip install .


vendas-cli data/vendasexemplo-python.csv --calc tudo --format text


⚙️ Parâmetros disponíveis
Parâmetro	Descrição
csv_path	Caminho para o arquivo CSV de vendas
--calc	Cálculo: total_produto, total_geral, itens, sku, mais_vendido, tudo
--start	Data inicial do filtro (opcional) - YYYY-MM-DD
--end	Data final do filtro (opcional) - YYYY-MM-DD
--format	text para tabela formatada ou json para estrutura JSON

ℹ️ Por padrão, se nenhum --calc for informado, será usado tudo.

📊 Exemplos de uso
bash
Copiar
Editar
# Tudo em formato JSON
vendas-cli data/vendasexemplo-python.csv --format json

# Total por produto (texto)
vendas-cli data/vendasexemplo-python.csv --calc total_produto --format text

# Total geral (JSON)
vendas-cli data/vendasexemplo-python.csv --calc total_geral --format json

# Tudo com filtro por data
vendas-cli data/vendasexemplo-python.csv --calc tudo --start 2024-01-01 --end 2024-03-31


Na pasta raiz do projeto (MIRANTE), execute:

bash
Copiar
Editar
pytest test/mirante_teste.py
Ou para rodar todos os testes:

bash
Copiar
Editar
pytest


👨‍💻 Autor
Jonathan de Oliveira Souza Filho
Golamp Tecnologia
https://golamp.com.br

