# 💰 Financial Risk & Revenue Analytics with DuckDB

Projeto de análise financeira desenvolvido utilizando SQL avançado, DuckDB e Streamlit com foco em analytics engineering e análise de risco de crédito.

O projeto simula um ambiente real de analytics financeiro encontrado em fintechs, bancos digitais e empresas orientadas a dados, utilizando arquitetura analítica moderna baseada em SQL-first analytics.

---

# 📌 Objetivo

Construir uma plataforma de análise financeira utilizando:

- DuckDB
- SQL avançado
- Python para orquestração
- Streamlit para visualização
- Dados reais de crédito
- Arquitetura analítica moderna

O foco principal do projeto é demonstrar habilidades avançadas em:

- Financial Analytics
- Analytics Engineering
- Data Warehousing
- OLAP Analytics
- Business Intelligence
- SQL avançado

---

# 🏦 Dataset

Dataset utilizado:

German Credit Risk Dataset

Contém informações sobre:

- Perfil de clientes
- Empréstimos
- Tempo de crédito
- Valor financiado
- Finalidade do crédito
- Tipo de moradia
- Risco financeiro

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Orquestração |
| DuckDB | Engine OLAP |
| SQL | Camada analítica |
| Streamlit | Dashboard |
| Plotly | Visualizações |
| Pandas | Manipulação de dados |
| Parquet | Export analítico |
| VS Code | Desenvolvimento |

---

# 🧠 Conceitos Aplicados

## SQL Avançado

- CTEs
- Window Functions
- Rolling Windows
- Statistical SQL
- Aggregations
- Ranking
- CASE WHEN
- Z-Score
- Data Marts

---

## Engenharia Analítica

- Staging Layer
- Analytics Layer
- Mart Layer
- SQL-first architecture
- Data pipeline
- OLAP modeling
- Export para Parquet

---

## Análises Financeiras

- Credit Risk Analysis
- Portfolio Analysis
- Customer Segmentation
- Outlier Detection
- Executive KPIs
- Loan Purpose Analysis
- Exposure Analysis

---

# 📂 Estrutura do Projeto

```bash
financial-credit-analytics/
│
├── data/
│   ├── raw/
│   ├── exports/
│   └── parquet/
│
├── sql/
│   ├── staging/
│   ├── analytics/
│   └── marts/
│
├── src/
│   ├── load_data.py
│   ├── run_pipeline.py
│   └── export_results.py
│
├── dashboard/
│   └── app.py
│
├── finance.db
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 Arquitetura do Projeto

O projeto foi desenvolvido separando:

## Camada Analítica

Executada localmente:

- DuckDB
- SQL
- processamento analítico
- criação de marts
- exportação para parquet

---

## Camada de Visualização

Executada no Streamlit Cloud:

- leitura dos arquivos parquet
- dashboards interativos
- visualização executiva

Essa arquitetura permite:

- dashboards leves
- deploy simples
- melhor performance
- menor uso de memória
- escalabilidade analítica

---

# 📊 Principais Análises

## Executive KPIs

- Total de clientes
- Volume financeiro
- Crédito médio
- Clientes de risco

---

## Risk Distribution

Distribuição percentual de clientes:

- Good Risk
- Bad Risk

---

## Financial Segmentation

Segmentação por:

- sexo
- moradia
- finalidade do crédito

---

## Loan Purpose Analysis

Análise de concentração financeira por produto:

- carro
- eletrônicos
- negócios
- educação
- móveis

---

## Outlier Detection

Detecção estatística de clientes fora do padrão utilizando:

Z-Score

---

## Rolling Credit Analysis

Análise de exposição financeira acumulada utilizando:

Window Functions

---

# 🚀 Como Executar

---

# 1️⃣ Clone o projeto

```bash
git clone <repo-url>
```

---

# 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 3️⃣ Adicione o dataset

Coloque o CSV em:

```bash
data/raw/
```

---

# 4️⃣ Execute o pipeline

```bash
python src/load_data.py
```

```bash
python src/run_pipeline.py
```

```bash
python src/export_results.py
```

---

# 5️⃣ Execute o dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Dashboard

O dashboard possui:

- KPIs executivos
- gráficos interativos
- análise de risco
- análise de produtos financeiros
- detecção de anomalias
- segmentação financeira

---

# 💾 Exportação Analítica

Os resultados das queries SQL são exportados para:

```bash
data/exports/
```

em formato:

```bash
.parquet
```

permitindo:

- melhor performance
- integração com BI
- deploy leve no Streamlit Cloud

---

# 📌 Resultados Obtidos

## Insights Financeiros

- ~39% da carteira concentrada em crédito automotivo
- clientes com imóvel próprio possuem maior volume financeiro
- existência de clientes altamente fora do padrão financeiro
- carteira relativamente pulverizada
- aproximadamente 30% da base apresenta risco elevado

---

# 🧮 Técnicas Estatísticas

## Z-Score

Utilizado para detecção de anomalias financeiras:

\[
z = \frac{x - \mu}{\sigma}
\]

---

# 📊 Exemplos de SQL Utilizados

## Window Function

```sql
RANK() OVER(
    ORDER BY credit_amount DESC
)
```

---

## Rolling Analysis

```sql
SUM(credit_amount) OVER(
    ORDER BY customer_id
    ROWS BETWEEN 9 PRECEDING AND CURRENT ROW
)
```

---

## Statistical SQL

```sql
STDDEV(credit_amount)
```

---

# ☁️ Deploy

O dashboard pode ser publicado gratuitamente utilizando:

- Streamlit Community Cloud

---

# 🏆 Habilidades Demonstradas

## Data Analytics

- análise financeira
- business intelligence
- analytics avançado

---

## SQL

- SQL avançado
- modelagem analítica
- OLAP
- window functions

---

## Engenharia de Dados

- pipelines
- parquet
- organização em camadas
- arquitetura analítica

---

# 🎯 Objetivo Profissional

Este projeto foi desenvolvido com foco em vagas como:

- Data Analyst
- Senior Data Analyst
- Analytics Engineer
- BI Analyst
- Financial Data Analyst
- Product Analyst

---

# 🛠️ Melhorias Futuras

- filtros interativos
- dashboard dark mode
- heatmaps
- star schema
- automação de pipeline
- integração com Power BI
- métricas financeiras avançadas

---

# 👨‍💻 Autor

Luis Turra

---

# 📄 Licença

Projeto desenvolvido para fins educacionais e de portfólio.