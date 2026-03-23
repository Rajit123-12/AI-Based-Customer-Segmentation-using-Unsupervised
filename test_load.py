from src.data_collection.load_data import load_data, basic_inspection

print("RUNNING TEST FILE")

df = load_data()
basic_inspection(df)
