from pathlib import Path
import pandas as pd
import re

BASE_DIR = Path(__file__).resolve().parent

dfs = [
    pd.read_csv(f)
    for f in sorted(BASE_DIR.glob("table_*.csv"))
]

def clean_columns(df):
    df.columns = [
        re.sub(r"\[.*?\]", "", col).strip()
        for col in df.columns
    ]
    return df

dfs = [clean_columns(df) for df in dfs]


from functools import reduce
wide_df = reduce(
    lambda left, right: pd.merge(left, right, on="Country", how="outer"),
    dfs
)
year_cols = [
    c for c in wide_df.columns
    if c.isdigit()
]
long_df = wide_df.melt(
    id_vars="Country",
    value_vars=year_cols,
    var_name="Year",
    value_name="Production"
)
long_df["Country"] = (
    long_df["Country"]
    .astype(str)
    .str.replace(r"\s*\[\d+\]", "", regex=True)
    .str.strip()
)



long_df["Year"] = long_df["Year"].astype(int)
long_df["Production"] = pd.to_numeric(long_df["Production"], errors="coerce")

long_df = long_df.sort_values(["Country", "Year"]).reset_index(drop=True)

# Keep only years >= 2018
long_df = long_df[long_df["Year"] >= 2018]

# Drop rows with any missing values in the three columns
long_df = long_df.dropna(subset=["Country", "Year", "Production"])

print(f"\nRows: {len(long_df)}")
print(f"Years: {long_df['Year'].min()} → {long_df['Year'].max()}")
print(long_df.isna().sum())
print(long_df["Year"].min())

OUTPUT_FILE = BASE_DIR / "vehicle_production.csv"
long_df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved to {OUTPUT_FILE}")
