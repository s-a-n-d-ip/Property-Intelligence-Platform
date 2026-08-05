from src.data.ingestion import load_data
from src.data.validation import validate_data

df = load_data("data/raw/flats.csv")

validate_data(df)