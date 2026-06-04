import pandas as pd
import glob
import os
from sqlalchemy import create_engine

PROCESSED_DIR = "data/processed"
engine = create_engine("sqlite:///bluestock_mf.db")

files = glob.glob(f"{PROCESSED_DIR}/*.csv")

for fpath in files:
    name = os.path.basename(fpath).replace("cleaned_", "").replace("_nav_raw.csv", "")
    df = pd.read_csv(fpath)
    df.to_sql(name, engine, if_exists="replace", index=False)
    print(f"Loaded {name} → {len(df)} rows into SQLite")

print("\nDatabase loaded! File: bluestock_mf.db")