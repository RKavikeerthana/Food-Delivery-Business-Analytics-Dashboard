
import pandas as pd


def create_dataset():
    df = pd.read_csv("orders.csv")

    # Convert order_date from text to a date format
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    return df
