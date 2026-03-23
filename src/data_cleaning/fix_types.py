import pandas as pd

def fix_types(df):
    print("\n[STEP 4] Fixing Data Types...")

    # Convert date column safely
    if "Dt_Customer" in df.columns:
        df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], errors="coerce")
        print("[INFO] Converted Dt_Customer to datetime")

    print("[INFO] Data types fixed")

    return df
