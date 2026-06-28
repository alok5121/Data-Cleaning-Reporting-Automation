import pandas as pd

# Remove duplicate rows
def remove_duplicates(df):
    return df.drop_duplicates()

# Fill missing values
def fill_missing_values(df):

    # Postal Code
    df["Postal Code"] = df["Postal Code"].fillna(df["Postal Code"].median())

    return df

# Convert dates
import pandas as pd

def convert_dates(df):

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True,
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True,
        errors="coerce"
    )

    return df

# Remove extra spaces
def clean_text(df):

    text_columns = [
        "Ship Mode",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Region",
        "Category",
        "Sub-Category",
        "Product Name"
    ]

    for col in text_columns:
        df[col] = df[col].str.strip()

    return df

# Standardize text
def standardize_text(df):

    df["Ship Mode"] = df["Ship Mode"].str.title()
    df["Segment"] = df["Segment"].str.title()
    df["Country"] = df["Country"].str.title()
    df["Region"] = df["Region"].str.title()
    df["Category"] = df["Category"].str.title()

    return df

# Convert Postal Code to integer
def convert_postal_code(df):

    df["Postal Code"] = df["Postal Code"].astype(int)

    return df