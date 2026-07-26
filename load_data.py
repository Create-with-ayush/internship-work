import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite
engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned CSVs
nav_df = pd.read_csv("data/processed/nav_history.csv")
transactions_df = pd.read_csv("data/processed/investor_transactions.csv")
performance_df = pd.read_csv("data/processed/scheme_performance.csv")

# Load into SQLite
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# Verify row counts
print("NAV Rows:", len(nav_df))
print("Transaction Rows:", len(transactions_df))
print("Performance Rows:", len(performance_df))

print("\nAll cleaned datasets loaded successfully!")