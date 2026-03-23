from sklearn.preprocessing import StandardScaler

def scale_data(df):
    print("\n[STEP 8] Scaling Data...")

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    print("[INFO] Scaling complete")

    return scaled_data
