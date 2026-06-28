import matplotlib.pyplot as plt

# Sales Distribution
def sales_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["Sales"], bins=30)

    plt.title("Sales Distribution")

    plt.xlabel("Sales")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("reports/charts/sales_distribution.png")

    plt.close()


# Category Count
def category_chart(df):

    plt.figure(figsize=(8,5))

    df["Category"].value_counts().plot(kind="bar")

    plt.title("Category Count")

    plt.tight_layout()

    plt.savefig("reports/charts/category_count.png")

    plt.close()


# Region Count
def region_chart(df):

    plt.figure(figsize=(8,5))

    df["Region"].value_counts().plot(kind="bar")

    plt.title("Region Count")

    plt.tight_layout()

    plt.savefig("reports/charts/region_count.png")

    plt.close()