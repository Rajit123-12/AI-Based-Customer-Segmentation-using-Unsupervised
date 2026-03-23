import pandas as pd

def encode_data(df):
    print("\n[STEP 7] Encoding Categorical Variables...")

    cat_cols = ["Education", "Marital_Status"]

    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    print(f"[INFO] Shape after encoding: {df.shape}")

    return df
