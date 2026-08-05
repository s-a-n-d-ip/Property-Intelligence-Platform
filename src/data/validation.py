import pandas as pd


def validate_data(df: pd.DataFrame):
    """
    Validate the dataset before processing.
    """

    print("=" * 60)
    print("DATA VALIDATION REPORT")
    print("=" * 60)

    # 1. Dataset Shape
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    # 2. Empty Dataset
    if df.empty:
        raise ValueError("Dataset is empty!")
    print("✓ Dataset is not empty.")

    # 3. Duplicate Rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows : {duplicates}")

    # 4. Missing Values
    print("\nMissing Values")
    print("-" * 60)

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values found.")
    else:
        missing_percent = (missing / len(df) * 100).round(2)

        missing_df = pd.DataFrame({
            "Missing Count": missing,
            "Percentage": missing_percent
        })

        print(missing_df.sort_values("Percentage", ascending=False))

    # 5. Data Types
    print("\nColumn Data Types")
    print("-" * 60)
    print(df.dtypes)

    # 6. Unique Values
    print("\nUnique Values")
    print("-" * 60)

    unique_df = pd.DataFrame({
        "Column": df.columns,
        "Unique Values": [df[col].nunique() for col in df.columns]
    })

    print(unique_df)

    # 7. Numerical Summary
    print("\nNumerical Summary")
    print("-" * 60)
    print(df.describe())

    print("=" * 60)
    print("VALIDATION COMPLETED")
    print("=" * 60)

    print("\nChecking Required Columns")
    print("-" * 60)

    required_columns = [
    "property_name",
    "link",
    "society",
    "price",
    "area",
    "areaWithType",
    "bedRoom",
    "bathroom",
    "balcony",
    "additionalRoom",
    "address",
    "floorNum",
    "facing",
    "agePossession",
    "nearbyLocations",
    "description",
    "furnishDetails",
    "features",
    "rating",
    "property_id"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing Required Columns: {missing_columns}"
        )

    print("✓ All required columns are present.")