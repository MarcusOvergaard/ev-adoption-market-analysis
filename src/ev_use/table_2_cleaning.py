# Load the data
import pandas as pd

df = pd.read_csv(r"C:\Users\marcu\Desktop\DataScraping\Cars_Data\Electric car use by country\table_2.csv")

df.columns = [
    "Region",
    "PEV_stock_23",
    "Annual_sales_23",
    "Market_share_23",
    "Share_of_cars_in_use_23"
]
# Remove references like [75], [iii], (2021) everywhere
import re

def strip_refs(x):
    if isinstance(x, str):
        return re.sub(r"\[.*?\]|\(.*?\)", "", x).strip()
    return x

df = df.applymap(strip_refs)

# Convert numeric columns properly
for col in ["PEV_stock_23", "Annual_sales_23"]:
    df[col] = (
        df[col]
        .str.replace(",", "", regex=False)
        .astype(int)
    )

#Percentages → floats
for col in ["Market_share_23", "Share_of_cars_in_use_23"]:
    df[col] = (
        df[col]
        .str.replace("%", "", regex=False)
        .astype(float)
    )
#Fix percentages
df["Market_share_23"] = (
    df["Market_share_23"] / 100
)
df["Share_of_cars_in_use_23"] = (
    df["Share_of_cars_in_use_23"] / 100
)

# Create % of global EV sales column
df["%_ev_sales_global"] = (
    df["Annual_sales_23"] / 13800000
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
out_path = BASE_DIR / "ev_2.csv"

df.to_csv(out_path, index=False)
