def drop_columns(df):
    print("\n[STEP 3] Dropping Columns...")

    cols_to_drop = ["ID"]

    existing_cols = [col for col in cols_to_drop if col in df.columns]

    if not existing_cols:
        print("[INFO] No columns to drop")
        return df

    df = df.drop(columns=existing_cols)

    print(f"[INFO] Dropped columns: {existing_cols}")
    print(f"[INFO] Remaining columns: {df.columns.tolist()}")

    return df
