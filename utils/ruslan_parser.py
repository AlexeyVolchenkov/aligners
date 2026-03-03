import csv
import os

# Имя входного CSV файла
csv_file = "metadata_RUSLAN_22200.csv"

# Имя выходной папки
output_dir = "out_lab"

# Создаём папку, если её нет
os.makedirs(output_dir, exist_ok=True)

# Читаем CSV и создаём .lab файлы
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        if len(row) >= 2:
            filename = row[0].strip() + ".lab"
            text = row[1].strip()

            # Полный путь к файлу
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as out_f:
                out_f.write(text)

print(f"Готово! Файлы сохранены в папку '{output_dir}'")