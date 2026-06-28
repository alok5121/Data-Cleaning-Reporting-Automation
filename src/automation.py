from data_loader import load_data

from cleaning import *

from reporting import *

from visualization import *

# Load Dataset
df = load_data("../data/raw/superstore_sales.csv")

print("Dataset Loaded")

# Cleaning
df = remove_duplicates(df)

df = fill_missing_values(df)

df = convert_dates(df)

df = clean_text(df)

df = standardize_text(df)

df = convert_postal_code(df)

print("Cleaning Completed")

# Report
report = generate_report(df)

for key, value in report.items():
    print(f"{key}: {value}")

# Save cleaned data
df.to_csv("../data/cleaned/cleaned_superstore_sales.csv", index=False)

# Charts
sales_distribution(df)

category_chart(df)

region_chart(df)

print("Project Completed Successfully")