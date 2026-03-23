from src.data_collection.load_data import load_data
from src.data_cleaning.handle_missing import handle_missing
from src.data_cleaning.drop_columns import drop_columns
from src.data_cleaning.fix_types import fix_types
from src.data_cleaning.remove_duplicates import remove_duplicates


if __name__ == "__main__":
    df = load_data()

    df = handle_missing(df)
    df = drop_columns(df)
    df = fix_types(df)
    df = remove_duplicates(df)

    print("\n[FINAL CLEANED DATA]")
    print(df.head())

    print(f"\n[INFO] Final Shape: {df.shape}")