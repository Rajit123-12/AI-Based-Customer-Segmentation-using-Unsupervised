from sklearn.metrics import silhouette_score
import numpy as np

def silhouette_analysis(data, k=3):
    print(f"\n[STEP 10] Silhouette Analysis for k={k}...")

    # 🔥 take sample (important)
    if data.shape[0] > 1000:
        idx = np.random.choice(data.shape[0], 1000, replace=False)
        data_sample = data[idx]
    else:
        data_sample = data

    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data_sample)

    score = silhouette_score(data_sample, labels)

    print(f"[INFO] Silhouette Score: {score:.4f}")