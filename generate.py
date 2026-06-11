import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["Product", "Price_USD", "Stock_Quantity", "Category"]

def generate_row():
    return {
        "Product": random.choice(["Мука", "Бананы", "Кофе", "Молоко", "Хлеб", "Яблоки", "Сыр"]),
        "Price_USD": round(random.uniform(0.5, 15.0), 2),
        "Stock_Quantity": random.randint(10, 500),
        "Category": random.choice(["Бакалея", "Фрукты", "Напитки", "Молочные продукты", "Выпечка"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

