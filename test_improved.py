from src.data_collection.load_data import load_data
from src.data_cleaning.handle_missing import handle_missing
from src.data_cleaning.drop_columns import drop_columns
from src.data_cleaning.fix_types import fix_types
from src.data_cleaning.remove_duplicates import remove_duplicates
from src.feature_engineering.feature_engineering import feature_engineering
from src.encoding_scaling.encoding import encode_data
from src.encoding_scaling.scaling import scale_data
from src.clustering.pca import apply_pca
from src.k_selection.silhouette import silhouette_analysis
from src.clustering.kmeans import apply_kmeans
from src.clustering.visualize_clusters import plot_clusters

df = load_data()

df = handle_missing(df)
df = drop_columns(df)
df = fix_types(df)
df = remove_duplicates(df)
df = feature_engineering(df)

df = encode_data(df)

# 🔥 KEEP IMPORTANT FEATURES ONLY
important_features = [
    "Income", "Age", "Total_Spend",
    "Total_Purchases", "Customer_Tenure"
]

df = df[important_features]

scaled = scale_data(df)

# PCA
reduced = apply_pca(scaled)

# Clustering
labels, model = apply_kmeans(reduced, k=3)

# Evaluate
silhouette_analysis(reduced, k=3)

# Plot
plot_clusters(reduced, labels)
from src.utils.save_results import save_results

save_results(df, labels)
