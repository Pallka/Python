import csv
import time

def count_ukraine_lines(file):
    count = 0
    with open(file, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['country'] == 'Ukraine':
                count += 1
    return count

file_path = "updated_data.csv"
start = time.time()
result = count_ukraine_lines(file_path)
print(f"\nРядків з 'country = Ukraine': {result}")
print(f"Час: {time.time() - start:.6f} с.")