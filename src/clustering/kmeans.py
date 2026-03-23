from sklearn.cluster import KMeans

def apply_kmeans(data, k=3):
    print(f"\n[STEP 11] Running KMeans with k={k}...")

    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)

    print("[INFO] Clustering complete")

    return labels, model
