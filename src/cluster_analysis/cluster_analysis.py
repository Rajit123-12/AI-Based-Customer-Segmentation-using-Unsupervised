def analyze_clusters(df):
    print("\n[STEP 12] Cluster Analysis...")

    important_cols = [
        "Income", "Age", "Total_Spend",
        "Total_Purchases", "Customer_Tenure",
        "Family_Size"
    ]

    summary = df.groupby("Cluster")[important_cols].mean()

    print("\n[CLUSTER SUMMARY]")
    print(summary)

    print("\n[CLUSTER INSIGHTS]")

    for cluster in summary.index:
        print(f"\nCluster {cluster}:")

        spend = summary.loc[cluster, "Total_Spend"]
        income = summary.loc[cluster, "Income"]

        if spend > summary["Total_Spend"].mean():
            print("High-value customers")
        elif spend < summary["Total_Spend"].mean():
            print("Low-value customers")
        else:
            print("Moderate customers")

        if income > summary["Income"].mean():
            print("High income group")
        else:
            print("Lower income group")

    return summary
