import pandas as pd
import os

def load_data(path="C:\\Users\\billo\\OneDrive\\Desktop\\AI-Based Customer Segmentation using Unsupervised\\SmartCart-Customer-Segmentation\\data\\raw\\data.csv"):
    print("[STEP 1] Loading Data...")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    print(f"[INFO] Shape: {df.shape}")
    return df


def basic_inspection(df):
    print("\n[INFO] Head:")
    print(df.head())

    print("\n[INFO] Info:")
    df.info()

    print("\n[INFO] Describe:")
    print(df.describe())