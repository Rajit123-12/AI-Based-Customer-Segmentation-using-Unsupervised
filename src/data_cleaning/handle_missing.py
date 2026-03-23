def handle_missing(df):
    print("\n[STEP 2] Handling Missing Values...")

    print("\n[INFO] Missing BEFORE:")
    print(df.isnull().sum())

    # Fill numeric columns
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical columns
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    print("\n[INFO] Missing AFTER:")
    print(df.isnull().sum())

    return df
