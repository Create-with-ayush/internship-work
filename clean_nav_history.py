import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(
    by=['amfi_code', 'date']
)

df['nav'] = (
    df.groupby('amfi_code')['nav']
      .ffill()
)

df = df.drop_duplicates(
    subset=['amfi_code', 'date']
)

df = df[df['nav'] > 0]

df.to_csv(
    "data/processed/nav_history.csv",
    index=False
)

print("NAV History cleaned successfully")