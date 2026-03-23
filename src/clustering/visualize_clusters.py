import matplotlib.pyplot as plt

def plot_clusters(data, labels):
    print("\n[STEP 14] Plotting Clusters...")

    plt.figure()
    plt.scatter(data[:,0], data[:,1], c=labels)

    plt.title("Customer Segments (PCA)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    plt.savefig("outputs/plots/clusters.png")
    plt.close()

    print("[INFO] Cluster plot saved")
