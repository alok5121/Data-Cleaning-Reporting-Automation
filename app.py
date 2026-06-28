import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaning Automation", layout="wide")

st.title("📊 Data Cleaning & Reporting Automation")

uploaded_file = st.file_uploader("Upload Superstore CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Original Dataset")

    st.dataframe(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))

    col2.metric("Columns", len(df.columns))

    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    if st.button("Clean Dataset"):

        df = df.drop_duplicates()

        df["Postal Code"] = df["Postal Code"].fillna(df["Postal Code"].median())

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

        st.success("Dataset Cleaned Successfully")

        st.dataframe(df)

        st.download_button(
            "Download Clean Dataset",
            df.to_csv(index=False),
            "cleaned_superstore.csv",
            "text/csv"
        )