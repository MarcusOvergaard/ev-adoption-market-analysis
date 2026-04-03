# Load the data
import pandas as pd
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
file = os.path.join(script_dir, "table_0.csv")
output_file = os.path.join(script_dir, "vehicles_per_capita.csv")

# Load the tables
table = pd.read_csv(file)

# Drop the Ref column
df = table.drop(columns=["Ref"])

# Fix column name
df = df.rename(columns={
    "Vehicles per 1,000 people": "vehicles_per_1000_people"
})


"""region_to_country = {
    # Crown dependencies / territories
    "Guernsey (UK)": "United Kingdom",
    "Jersey (UK)": "United Kingdom",
    "Guam (US)": "United States",
    # Danish territories
    "Faroe Islands (Denmark)": "Denmark",
    "Greenland (Denmark)": "Denmark",
    # Chinese SARs
    "Hong Kong (China)": "China",
    "Macao (China)": "China",
    # Political edge case
    "Taiwan": "Taiwan",  # keep separate (explicit choice)
}
"""
df["Country"] = df["Region"]

df = df.drop(columns=["Region"])

# Keep only years >= 2018
df = df[df["Year"] >= 2018]

# Save the combined table in the same folder as the script
df.to_csv(output_file, index=False)

print(f"Combined file saved at: {output_file}")



