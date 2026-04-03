import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_motor_vehicles_per_capita"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
html = response.text

# Parse all tables
dfs = pd.read_html(html)

print(f"Found {len(dfs)} tables")  # lets you see how many there are

# Save each table separately
for i, df in enumerate(dfs):
    filename = f"table_{i}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")


for i, df in enumerate(dfs):
    if df.empty or df.shape[1] < 2:
        continue  # skip tiny or empty tables
    df.to_csv(f"table_{i}.csv", index=False)


for i, df in enumerate(dfs):
    first_col = df.iloc[:, 0].astype(str)
    if first_col.str.contains(r"\d{4}").any():  # table has years
        df.to_csv(f"table_{i}.csv", index=False)
