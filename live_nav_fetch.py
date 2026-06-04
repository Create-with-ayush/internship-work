import requests
import pandas as pd
import os

OUTPUT_FOLDER = "data/raw"

funds = {
    "hdfc_top100_direct": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = f"{OUTPUT_FOLDER}/{fund_name}.csv"

        nav_df.to_csv(
            file_path,
            index=False
        )

        print(f"Saved: {file_path}")

    else:

        print(
            f"Failed to fetch {fund_name}"
        )
    
try:

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

except Exception as e:

    print(
        f"Error fetching {fund_name}: {e}"
    )