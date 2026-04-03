# Load the data
import pandas as pd
import re
import numpy as np
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
file = os.path.join(script_dir, "table_3.csv")
output_file = os.path.join(script_dir, "ev_market_share_by_country_year.csv")

# Load the tables
df = pd.read_csv(file)

# Clean column names
df.columns = [
    re.sub(r"\[.*?\]", "", col).strip()
    for col in df.columns
]

# Clean Country column
df['Country'] = df['Country'].apply(lambda x: re.sub(r"\[.*?\]", "", x).strip() if isinstance(x, str) else x)

# Remove reference noise inside cells
def clean_cell(x):
    if isinstance(x, str):
        x = re.sub(r"\[.*?\]", "", x)   # remove [75], [ii], etc.
        x = re.sub(r"\(.*?\)", "", x)   # remove (BEVs only)
        x = x.replace("—", "").strip()  # remove em-dash
        if x == "":
            return np.nan
        return x
    return x

# Convert year columns to numeric percentages
for col in df.columns:
    if col != "Country":
        df[col] = df[col].str.replace("%", "", regex=False)  # remove %
        df[col] = pd.to_numeric(df[col], errors="coerce")    # coerce non-numbers to NaN


# Convert from wide to long
year_cols = [c for c in df.columns if c != "Country"]

df_long = df.melt(
    id_vars="Country",
    value_vars=year_cols,
    var_name="Year",
    value_name="EV_market_share"
)

# Convert Year to int
df_long["Year"] = df_long["Year"].astype(int)

# Keep only years >= 2018
df_long = df_long[df_long["Year"] >= 2018]

# Drop rows with any missing values in the three columns
df_long = df_long.dropna(subset=["Country", "Year", "EV_market_share"])

print(f"\nRows: {len(df_long)}")
print(f"Years: {df_long['Year'].min()} → {df_long['Year'].max()}")
print(df_long.isna().sum())
print(df_long["Year"].min())

# Save the combined table in the same folder as the script
df_long.to_csv(output_file, index=False)

print(f"Combined file saved at: {output_file}")
