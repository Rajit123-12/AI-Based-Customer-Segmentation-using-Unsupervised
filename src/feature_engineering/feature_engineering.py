import pandas as pd
from datetime import datetime

def feature_engineering(df):
    print("\n[STEP 6] Feature Engineering...")

    # Age
    current_year = datetime.now().year
    df["Age"] = current_year - df["Year_Birth"]

    # Customer Tenure
    if "Dt_Customer" in df.columns:
        df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], errors='coerce')

        today = pd.to_datetime("today")
        df["Customer_Tenure"] = (today - df["Dt_Customer"]).dt.days

        # ? FIXED (NO inplace)
        df["Customer_Tenure"] = df["Customer_Tenure"].fillna(
            df["Customer_Tenure"].median()
        )

    # Total Spend
    spend_cols = [
        "MntWines","MntFruits","MntMeatProducts",
        "MntFishProducts","MntSweetProducts","MntGoldProds"
    ]
    df["Total_Spend"] = df[spend_cols].sum(axis=1)

    # Total Purchases
    purchase_cols = [
        "NumWebPurchases","NumCatalogPurchases","NumStorePurchases"
    ]
    df["Total_Purchases"] = df[purchase_cols].sum(axis=1)

    # Family Size
    df["Family_Size"] = df["Kidhome"] + df["Teenhome"] + 1

    print("[INFO] Feature Engineering Complete")

    return df
