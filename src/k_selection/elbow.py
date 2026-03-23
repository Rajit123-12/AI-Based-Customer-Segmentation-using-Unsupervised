from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def elbow_method(data):
    print("\n[STEP 9] Running Elbow Method...")

    inertia = []
    K = range(1, 11)

    for k in K:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(data)
        inertia.append(model.inertia_)

    plt.figure()
    plt.plot(K, inertia, 'bx-')
    plt.xlabel('K')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.savefig('outputs/plots/elbow.png')
    plt.close()

    print("[INFO] Elbow plot saved in outputs/plots/")
    return inertia
