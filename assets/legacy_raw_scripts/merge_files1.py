import pandas as pd
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
file_2024 = os.path.join(script_dir, "table_0.csv")
file_2023 = os.path.join(script_dir, "table_1.csv")
output_file = os.path.join(script_dir, "trade_data.csv")

# Load the tables
table_2024 = pd.read_csv(file_2024)
table_2023 = pd.read_csv(file_2023)

# Rename columns for clarity
table_2024 = table_2024.rename(columns={
    "Value exported (thousands USD)": "Value exported 2024",
    "Value imported (thousands USD)": "Value imported 2024",
    "Trade balance (thousands USD)": "Trade balance 2024"
})

table_2023 = table_2023.rename(columns={
    "Trade Value": "Value exported 2023"  # adjust if more columns exist
})

# Merge tables
combined = table_2024.merge(table_2023, on="Country", how="left")

# Correct numeric conversion
cols_to_numeric = [
    "Value exported 2024",
    "Value imported 2024"
]
for col in cols_to_numeric:
    combined[col] = (
        combined[col]
        .astype(str)
        .str.replace(",", "", regex=False)      # remove thousands separators
        .str.replace("−", "-", regex=False)     # fix Unicode minus
        .pipe(pd.to_numeric, errors="coerce")
    )

# Calculate the trade balance (don’t trust the source)
combined["Trade balance 2024"] = (
    combined["Value exported 2024"] -
    combined["Value imported 2024"]
)

# Check:
print(combined[cols_to_numeric].dtypes)
print(combined[combined[cols_to_numeric].isna().any(axis=1)])

# Save the combined table in the same folder as the script
combined.to_csv(output_file, index=False)

print(f"Combined file saved at: {output_file}")
