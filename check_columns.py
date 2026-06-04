import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\n===== FUND MASTER COLUMNS =====")
print(fund_master.columns.tolist())

print("\n===== NAV HISTORY COLUMNS =====")
print(nav_history.columns.tolist())

print("\n===== FUND MASTER SAMPLE =====")
print(fund_master.head())

print("\n===== NAV HISTORY SAMPLE =====")
print(nav_history.head())