from src.data_collection.load_data import load_data
from src.data_cleaning.handle_missing import handle_missing
from src.data_cleaning.drop_columns import drop_columns
from src.data_cleaning.fix_types import fix_types
from src.data_cleaning.remove_duplicates import remove_duplicates
from src.feature_engineering.feature_engineering import feature_engineering
from src.encoding_scaling.encoding import encode_data
from src.encoding_scaling.scaling import scale_data

df = load_data()

df = handle_missing(df)
df = drop_columns(df)
df = fix_types(df)
df = remove_duplicates(df)
df = feature_engineering(df)

df = encode_data(df)

# Keep only numeric columns
df_numeric = df.select_dtypes(include=['number'])

scaled = scale_data(df_numeric)

print("\n[FINAL SCALED DATA SHAPE]")
print(scaled.shape)
