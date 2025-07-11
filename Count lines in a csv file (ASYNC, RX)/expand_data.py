import pandas as pd
import math

def expand_data(input_file, output_file, target_rows):
    df = pd.read_csv(input_file)
    original_rows = len(df)
    print(f"Оригінальна кількість рядків: {original_rows}")

    if original_rows == 0:
        print("Файл не містить рядків. Немає що копіювати.")
        return

    multiplier = math.ceil(target_rows / original_rows)

    expanded_df = pd.concat([df] * multiplier, ignore_index=True)
    expanded_df = expanded_df[:target_rows]

    expanded_df.to_csv(output_file, index=False)
    print(f"Збережено файл '{output_file}' з {len(expanded_df)} рядками.")

file_path = "filtered.csv"
updated_file = "updated_data.csv"
target_data_size = 50000
expand_data(file_path, updated_file, target_data_size)