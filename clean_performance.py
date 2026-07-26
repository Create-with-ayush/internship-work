import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("===== DATA LOADED SUCCESSFULLY =====")
print("Rows:", len(df))

# -----------------------------
# STEP 1 : Check Missing Values
# -----------------------------
print("\n===== Missing Values =====")
print(df.isnull().sum())

# -----------------------------
# STEP 2 : Validate Return Columns
# -----------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\n===== Missing Return Values =====")
print(df[return_columns].isnull().sum())

# -----------------------------
# STEP 3 : Check Expense Ratio
# -----------------------------

expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:", len(expense_anomalies))

# Save anomalies separately
expense_anomalies.to_csv(
    "data/processed/expense_ratio_anomalies.csv",
    index=False
)

# -----------------------------
# STEP 4 : Check Negative AUM
# -----------------------------

negative_aum = df[df["aum_crore"] < 0]

print("Negative AUM Rows:", len(negative_aum))

# -----------------------------
# STEP 5 : Check Morningstar Rating
# -----------------------------

invalid_rating = df[
    (df["morningstar_rating"] < 1) |
    (df["morningstar_rating"] > 5)
]

print("Invalid Ratings:", len(invalid_rating))

# -----------------------------
# STEP 6 : Remove Duplicate Schemes
# -----------------------------

duplicates = df.duplicated(
    subset=["amfi_code"]
).sum()

print("Duplicate AMFI Codes:", duplicates)

df = df.drop_duplicates(
    subset=["amfi_code"]
)

# -----------------------------
# STEP 7 : Save Cleaned File
# -----------------------------

df.to_csv(
    "data/processed/scheme_performance.csv",
    index=False
)

print("\nScheme Performance cleaned successfully!")



