import pandas as pd

def load_data(filepath):
    """Load dataset and perform initial preprocessing."""
    df = pd.read_csv(filepath, encoding="ISO-8859-1")

    # Drop missing CustomerID
    df.dropna(subset=["CustomerID"], inplace=True)

    # Remove transactions with negative or zero quantities
    df = df[df["Quantity"] > 0]

    # Convert InvoiceNo to string
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)

    return df

if __name__ == "__main__":
    df = load_data("../data/retail_data.csv")
    print(df.head())

