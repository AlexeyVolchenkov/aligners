#!/bin/bash

# Использование: ./run_mfa.sh /путь/к/корпусу /путь/к/выходному/каталогу

CORPUS_PATH="$1"
OUTPUT_PATH="$2"

if [ $# -lt 2 ]; then
    echo "Ошибка: укажите путь к корпусу и выходному каталогу"
    echo "Пример: ./run_mfa.sh /home/user/corpus /home/user/output"
    exit 1
fi

# 2. Создание окружения
conda create -n aligner -c conda-forge montreal-forced-aligner -y

# 3. Активация окружения
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate aligner

echo "Используется корпус: $CORPUS_PATH"

# 4. Скачивание акустической модели
mfa model download acoustic russian_mfa

# 5. Скачивание словаря
mfa model download dictionary russian_mfa

# 6. Проверка корпуса
mfa validate "$CORPUS_PATH" russian_mfa russian_mfa

# 7. Запуск выравнивания
mfa align "$CORPUS_PATH" russian_mfa russian_mfa "$OUTPUT_PATH"

echo "Готово. Результаты в $OUTPUT_PATH"