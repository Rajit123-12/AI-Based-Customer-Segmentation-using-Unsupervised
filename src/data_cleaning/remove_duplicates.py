def remove_duplicates(df):
    print("\n[STEP 5] Removing Duplicates...")

    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print(f"[INFO] Removed {before - after} duplicates")

    return df
