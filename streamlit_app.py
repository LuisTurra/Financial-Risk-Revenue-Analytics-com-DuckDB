from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# MELHOR PATHS
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

EXPORT_DIR = BASE_DIR / "data" / "exports"

# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="Financial Risk Analytics",
    page_icon="💰",
    layout="wide"
)

# =====================================
# DATA LOAD
# =====================================

@st.cache_data
def load_data():

    data = {

        "kpis": pd.read_parquet(
            EXPORT_DIR / "kpis.parquet"
        ),

        "risk": pd.read_parquet(
            EXPORT_DIR / "risk_distribution.parquet"
        ),

        "loan": pd.read_parquet(
            EXPORT_DIR / "loan_purpose.parquet"
        ),

        "segmentation": pd.read_parquet(
            EXPORT_DIR / "financial_segmentation.parquet"
        ),

        "anomalies": pd.read_parquet(
            EXPORT_DIR / "anomalies.parquet"
        )
    }

    return data

data = load_data()

kpis = data["kpis"]
risk = data["risk"]
loan = data["loan"]
segmentation = data["segmentation"]
anomalies = data["anomalies"]



st.title("💰 Dashboard de Análise Financeira")


# =====================================
# KPI 
# =====================================

st.subheader("Indicadores Executivos")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Clientes",
    f"{int(kpis['total_clients'][0]):,}"
)

col2.metric(
    "Volume de Crédito",
    f"${kpis['total_credit_volume'][0]:,.0f}"
)

col3.metric(
    "Crédito Médio",
    f"${kpis['avg_credit'][0]:,.0f}"
)

col4.metric(
    "Clientes de Risco",
    f"{int(kpis['risky_clients'][0]):,}"
)

# =====================================
# DISTRIBUIÇÂO DE RISCO
# =====================================

st.subheader("Distribuição de Risco")
risk["risk_label"] = risk["risk_label"].replace({
    "good": "Bom",
    "bad": "Ruim"
})
fig_risk = px.pie(
    risk,
    names="risk_label",
    values="total_clients",
    
    hole=0.4
)

st.plotly_chart(
    fig_risk,
    
    use_container_width=True
)

# =====================================
# EMPRÉSTIMOS
# =====================================

st.subheader("Finalidade dos Empréstimos")
loan["purpose"] = loan["purpose"].replace({

    "car": "Carro",

    "radio/TV": "Eletrônicos",

    "furniture/equipment": "Móveis",

    "business": "Negócios",

    "education": "Educação",

    "repairs": "Reparos",

    "domestic appliances": "Eletrodomésticos",

    "vacation/others": "Outros"

})
fig_loan = px.bar(
    loan.sort_values(
        "total_credit_volume",
        ascending=False
    ),

    x="purpose",

    y="total_credit_volume",

    labels={
        "purpose": "Finalidade",
        "total_credit_volume": "Volume Financeiro"
    },

    text_auto=True
)

st.plotly_chart(
    fig_loan,
    use_container_width=True
)

# =====================================
# SEGMENTOS
# =====================================

st.subheader("Principais Segmentos Financeiros")

st.dataframe(
    segmentation.head(10),
    use_container_width=True
)

# =====================================
# PADRÃO
# =====================================

st.subheader("Clientes Fora do Padrão")

fig_outliers = px.scatter(

    anomalies,

    x="customer_id",

    y="credit_amount",

    labels={

        "customer_id": "Cliente",

        "credit_amount": "Valor do Crédito"

    }
)

st.plotly_chart(
    fig_outliers,
    use_container_width=True
)

st.dataframe(
    anomalies,
    use_container_width=True
)