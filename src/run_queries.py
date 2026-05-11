import duckdb

con = duckdb.connect("finance.db")

# cria staging
staging_query = open(
    "sql/staging/stg_credit.sql"
).read()

con.execute(staging_query)

# executa analytics
analytics_query = open(
    "sql/analytics/kpis.sql"
).read()

result = con.execute(
    analytics_query
).fetchdf()

print(result)