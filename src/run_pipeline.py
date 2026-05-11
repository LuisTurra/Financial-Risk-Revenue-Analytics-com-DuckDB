import duckdb

con = duckdb.connect("finance.db")

queries = [

    "sql/staging/stg_credit.sql",

    "sql/analytics/kpis.sql",

    "sql/analytics/financial_segmentation.sql",

    "sql/analytics/customer_ranking.sql",

    "sql/analytics/risk_distribution.sql",

    "sql/analytics/age_risk_analysis.sql",

    "sql/analytics/rolling_credit.sql",

    "sql/analytics/loan_purpose_analysis.sql",

    "sql/analytics/anomaly_detection.sql",

    "sql/marts/financial_summary.sql"
]

for file in queries:

    print(f"\nExecutando: {file}")

    query = open(file, encoding="utf-8").read()

    if query.strip().lower().startswith("select"):
        result = con.execute(query).fetchdf()
        print(result.head())
    else:
        con.execute(query)
        print("Query executada.")