import duckdb
import pandas as pd

con = duckdb.connect("finance.db")

df = pd.read_csv(
    "data/raw/german_credit_data_updated.csv"
)

# remove coluna inútil
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# normaliza nomes
df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
)

print(df.columns.tolist())

con.execute("""
CREATE OR REPLACE TABLE credit_data AS
SELECT * FROM df
""")

print("Tabela criada.")