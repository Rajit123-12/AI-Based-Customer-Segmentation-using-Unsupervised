from src.data_collection.load_data import load_data
from src.data_cleaning.handle_missing import handle_missing
from src.data_cleaning.drop_columns import drop_columns
from src.data_cleaning.fix_types import fix_types
from src.data_cleaning.remove_duplicates import remove_duplicates
from src.feature_engineering.feature_engineering import feature_engineering
from src.encoding_scaling.encoding import encode_data
from src.encoding_scaling.scaling import scale_data
from src.k_selection.elbow import elbow_method
from src.k_selection.silhouette import silhouette_analysis
from src.clustering.kmeans import apply_kmeans
from src.cluster_analysis.cluster_analysis import analyze_clusters
df = load_data()

df = handle_missing(df)
df = drop_columns(df)
df = fix_types(df)
df = remove_duplicates(df)
df = feature_engineering(df)

df = encode_data(df)

df_numeric = df.select_dtypes(include=['number'])
df_numeric = df_numeric.fillna(df_numeric.median())

scaled = scale_data(df_numeric)

scaled = scale_data(df_numeric)

# Step 1: Elbow
elbow_method(scaled)

# Step 2: Try k=3 (you can adjust after seeing elbow)
silhouette_analysis(scaled, k=3)

# Step 3: Final clustering
labels, model = apply_kmeans(scaled, k=3)

# assign clusters
df["Cluster"] = labels

print("\n[CLUSTERED DATA]")
print(df["Cluster"].value_counts())

# 🔥 ADD THIS LINE (VERY IMPORTANT)
analyze_clusters(df)

# save output
df.to_csv("outputs/clustered_data.csv", index=False)