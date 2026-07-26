import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Check transaction types
print("Transaction Types:")
print(df["transaction_type"].unique())

# Validate amount
df = df[df["amount_inr"] > 0]

# Convert date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions.csv",
    index=False
)

print("\nInvestor Transactions cleaned successfully!")