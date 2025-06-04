import csv
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")

def load_fallback_data(ano: int, categoria: str, subcategoria: str):
    filename = f"{categoria}_{subcategoria}_{ano}.csv"
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)