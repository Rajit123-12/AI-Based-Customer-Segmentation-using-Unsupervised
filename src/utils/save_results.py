import pandas as pd

def save_results(df, labels):
    print("\n[STEP 15] Saving Results...")

    df["Cluster"] = labels
    df.to_csv("outputs/final_clusters.csv", index=False)

    print("[INFO] Saved to outputs/final_clusters.csv")
