import pandas as pd

def generate_report(df):

    report = {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing Values": df.isnull().sum().sum(),

        "Duplicate Rows": df.duplicated().sum(),

        "Total Sales": round(df["Sales"].sum(),2),

        "Average Sales": round(df["Sales"].mean(),2),

        "Maximum Sales": round(df["Sales"].max(),2),

        "Minimum Sales": round(df["Sales"].min(),2)

    }

    return report