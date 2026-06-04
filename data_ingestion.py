import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [
    file
    for file in os.listdir(DATA_FOLDER)
    if file.endswith(".csv")
]

print("CSV Files Found:\n")

for file in csv_files:

    print("\n")
    print("=" * 60)
    print("FILE:", file)
    print("=" * 60)

    path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum()

    print("\nDuplicate Rows:")
    print(duplicates)

    empty_columns = df.columns[df.isnull().all()]

    print("\nCompletely Empty Columns:")

    if len(empty_columns) > 0:
        print(empty_columns)
    else:
        print("None")

    print("\nDataset Info:")
    print(df.info())