import duckdb
import os
from pathlib import Path

con = duckdb.connect("finance.db")

EXPORT_DIR = "data/exports"

os.makedirs(EXPORT_DIR, exist_ok=True)

queries = {

    "kpis":
        "sql/analytics/kpis.sql",

    "risk_distribution":
        "sql/analytics/risk_distribution.sql",

    "financial_segmentation":
        "sql/analytics/financial_segmentation.sql",

    "loan_purpose":
        "sql/analytics/loan_purpose_analysis.sql",

    "anomalies":
        "sql/analytics/anomaly_detection.sql"
}

for output_name, sql_file in queries.items():

    print(f"Exportando: {output_name}")

    query = Path(sql_file).read_text(
        encoding="utf-8"
    )

    # remove ;
    query = query.strip().rstrip(";")

    output_path = (
        f"{EXPORT_DIR}/{output_name}.parquet"
    )

    con.execute(f"""
        COPY (
            {query}
        )
        TO '{output_path}'
        (FORMAT PARQUET)
    """)

    print(f"Salvo em: {output_path}")