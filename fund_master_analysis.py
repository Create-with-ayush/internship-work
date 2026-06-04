import pandas as pd

# ==========================
# Load Data
# ==========================

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 80)
print("FUND MASTER ANALYSIS")
print("=" * 80)

# ==========================
# Dataset Overview
# ==========================

print("\nFund Master Shape:")
print(fund_master.shape)

print("\nNAV History Shape:")
print(nav_history.shape)

# ==========================
# Unique Fund Houses
# ==========================

print("\n" + "=" * 80)
print("UNIQUE FUND HOUSES")
print("=" * 80)

fund_houses = sorted(fund_master["fund_house"].unique())

for house in fund_houses:
    print(house)

print("\nTotal Fund Houses:", fund_master["fund_house"].nunique())

# ==========================
# Unique Categories
# ==========================

print("\n" + "=" * 80)
print("UNIQUE CATEGORIES")
print("=" * 80)

categories = sorted(fund_master["category"].unique())

for category in categories:
    print(category)

print("\nTotal Categories:", fund_master["category"].nunique())

# ==========================
# Unique Sub Categories
# ==========================

print("\n" + "=" * 80)
print("UNIQUE SUB-CATEGORIES")
print("=" * 80)

sub_categories = sorted(fund_master["sub_category"].unique())

for sub in sub_categories:
    print(sub)

print("\nTotal Sub Categories:", fund_master["sub_category"].nunique())

# ==========================
# Unique Risk Grades
# ==========================

print("\n" + "=" * 80)
print("UNIQUE RISK CATEGORIES")
print("=" * 80)

risk_categories = sorted(fund_master["risk_category"].unique())

for risk in risk_categories:
    print(risk)

print("\nTotal Risk Categories:", fund_master["risk_category"].nunique())

# ==========================
# Missing Values
# ==========================

print("\n" + "=" * 80)
print("MISSING VALUES")
print("=" * 80)

print(fund_master.isnull().sum())

# ==========================
# Duplicate Rows
# ==========================

duplicates = fund_master.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

# ==========================
# AMFI CODE VALIDATION
# ==========================

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

master_codes = set(
    fund_master["amfi_code"].astype(str)
)

nav_codes = set(
    nav_history["amfi_code"].astype(str)
)

missing_codes = master_codes - nav_codes

print(
    "\nTotal AMFI Codes in Fund Master:",
    len(master_codes)
)

print(
    "Total AMFI Codes in NAV History:",
    len(nav_codes)
)

print(
    "Missing AMFI Codes:",
    len(missing_codes)
)

if len(missing_codes) > 0:

    print("\nMissing Codes:")

    for code in sorted(missing_codes):
        print(code)

else:

    print(
        "\nAll AMFI codes exist in NAV History."
    )

# ==========================
# Save Missing Codes
# ==========================

missing_df = pd.DataFrame(
    {
        "missing_amfi_code":
        list(missing_codes)
    }
)

missing_df.to_csv(
    "reports/missing_amfi_codes.csv",
    index=False
)

# ==========================
# Scheme Counts by Fund House
# ==========================

print("\n" + "=" * 80)
print("SCHEME COUNT BY FUND HOUSE")
print("=" * 80)

house_count = (
    fund_master
    .groupby("fund_house")
    ["amfi_code"]
    .count()
    .sort_values(ascending=False)
)

print(house_count)

# ==========================
# Scheme Counts by Category
# ==========================

print("\n" + "=" * 80)
print("SCHEME COUNT BY CATEGORY")
print("=" * 80)

category_count = (
    fund_master
    .groupby("category")
    ["amfi_code"]
    .count()
    .sort_values(ascending=False)
)

print(category_count)

# ==========================
# Summary
# ==========================

print("\n" + "=" * 80)
print("DATA QUALITY SUMMARY")
print("=" * 80)

print(
    f"Total Schemes: {len(fund_master)}"
)

print(
    f"Unique AMFI Codes: {fund_master['amfi_code'].nunique()}"
)

print(
    f"Fund Houses: {fund_master['fund_house'].nunique()}"
)

print(
    f"Categories: {fund_master['category'].nunique()}"
)

print(
    f"Sub Categories: {fund_master['sub_category'].nunique()}"
)

print(
    f"Risk Categories: {fund_master['risk_category'].nunique()}"
)

print(
    f"Duplicate Rows: {duplicates}"
)

print(
    f"Missing AMFI Codes: {len(missing_codes)}"
)

print("\nAnalysis Completed Successfully.")