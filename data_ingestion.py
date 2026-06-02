import pandas as pd
import glob
import os

RAW_DIR = "data/raw"
files = glob.glob(f"{RAW_DIR}/*.csv")

print(f"Found {len(files)} CSV files\n")

for fpath in files:
    name = os.path.basename(fpath)
    df = pd.read_csv(fpath)
    print(f"Dataset: {name}")
    print(f"  Shape : {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Head:\n{df.head(2)}\n")

print("Data ingestion complete!")