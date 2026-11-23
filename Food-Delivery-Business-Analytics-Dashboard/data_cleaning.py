
def clean_dataset(df):
    print("\n--- DATA QUALITY REPORT ---")

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Check duplicate rows
    duplicate_rows = df.duplicated().sum()
    print("\nDuplicate rows:", duplicate_rows)

    # Check duplicate order IDs
    duplicate_ids = df["order_id"].duplicated().sum()
    print("Duplicate order IDs:", duplicate_ids)

    # Create a separate cleaned copy
    clean_df = df.drop_duplicates().copy()

    print("\nOriginal rows:", len(df))
    print("Rows after removing exact duplicates:", len(clean_df))

    return clean_df
