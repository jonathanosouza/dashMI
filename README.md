# 📊 Vendas CLI – Relatório de Vendas Mirante

Um gerador de relatórios de vendas via linha de comando, desenvolvido em Python, com suporte a filtros, formatos e métricas úteis.

---

## ✅ Funcionalidades

- Total por produto vendido  
- Valor total de vendas  
- Total de itens vendidos  
- Contagem de SKUs distintos  
- Produto mais vendido  
- Filtros por data  
- Saída em formato `text` (tabela) ou `json`

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/jonathanosouza/dashMI.git
cd mirante
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

Instale o pacote localmente:

```bash
cd vendas_cli
pip install .
```

---

## ▶️ Execute pela linha de comando

```bash
python -m vendas_cli data/vendasexemplo-python.csv --calc tudo --format text
```

---

## 🔧 Parâmetros disponíveis

| Parâmetro     | Descrição |
|---------------|-----------|
| `csv_path`    | Caminho para o arquivo CSV de vendas |
| `--calc`      | Tipo de cálculo: `total_produto`, `total_geral`, `itens`, `sku`, `mais_vendido`, `tudo` |
| `--start`     | Data inicial no formato `YYYY-MM-DD` (opcional) |
| `--end`       | Data final no formato `YYYY-MM-DD` (opcional) |
| `--format`    | Tipo de saída: `text` ou `json` |
| `--engine`    | Tipo de saída: `text` ou `json porém com pandas` |

---

## 💡 Exemplos de uso

###  Output padrão que gera todas as informações

```bash
python -m vendas_cli data/vendasexemplo-python.csv --format json
python -m vendas_cli data/vendasexemplo-python.csv --format text
```

### Executa tudo com saída formatada em texto

```bash
python -m vendas_cli data/vendasexemplo-python.csv --calc tudo --format text
```

### Apenas total por produto (tabela)

```bash
python -m vendas_cli data/vendasexemplo-python.csv --calc total_produto --format text
```

### Total geral de vendas em JSON

```bash
python -m vendas_cli data/vendasexemplo-python.csv --calc total_geral --format json
```

### Tudo com filtro de data

```bash
python -m vendas_cli data/vendasexemplo-python.csv --calc tudo --start 2024-01-01 --end 2024-03-31
```

---

## Testes com Pytest

### Para executar os testes automatizados com `pytest` na pasta raiz `mirante`:

```bash
pytest test/mirante_teste.py
```

### Ou simplesmente:

```bash
pytest
```

---

## 👨‍💻 Autor

**Jonathan de Oliveira Souza Filho** – Para Mirante Tecnologia 🚀
