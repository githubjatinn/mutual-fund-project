import requests
import pandas as pd
import os
from datetime import datetime

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

SCHEMES = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}

for name, code in SCHEMES.items():
    print(f"Fetching {name}...")
    url = f"https://api.mfapi.in/mf/{code}"
    r = requests.get(url, timeout=10)
    data = r.json()
    df = pd.DataFrame(data["data"])
    df["scheme_name"] = name
    df["scheme_code"] = code
    fpath = f"{RAW_DIR}/{name}_nav_raw.csv"
    df.to_csv(fpath, index=False)
    print(f"  Saved {len(df)} records → {fpath}")

print("\nAll NAV data fetched successfully!")