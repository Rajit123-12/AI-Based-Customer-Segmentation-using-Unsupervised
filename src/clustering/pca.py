from sklearn.decomposition import PCA

def apply_pca(data, n_components=2):
    print("\n[STEP 13] Applying PCA...")

    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(data)

    print(f"[INFO] Reduced shape: {reduced.shape}")
    print(f"[INFO] Explained variance: {pca.explained_variance_ratio_}")

    return reduced
