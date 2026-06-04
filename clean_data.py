import pandas as pd
import os
import glob

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

files = glob.glob(f"{RAW_DIR}/*.csv")

for fpath in files:
    name = os.path.basename(fpath)
    df = pd.read_csv(fpath)
    df.columns = df.columns.str.strip().str.lower()
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    out = f"{PROCESSED_DIR}/cleaned_{name}"
    df.to_csv(out, index=False)
    print(f"Cleaned {name} → {df.shape[0]} rows saved")

print("\nData cleaning complete!")