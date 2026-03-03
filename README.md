# Aligners
## MFA

1. Скачать [conda](https://www.anaconda.com/download)
2. Сделать окружение в которое сразу установить mfa
```commandline
conda create -n aligner -c conda-forge montreal-forced-aligner
```
3. Активируем окружение, если это не произойдет автоматически
```commandline
conda activate aligner
```
4. Делаем корпус в каталоге, где .wav файлы и с таким же названием .lab, где находится текстовая транскрипция
5. Скачать акустическую модель
```commandline
mfa model download acoustic russian_mfa
```
6. Скачать словарь
```commandline
mfa model download dictionary russian_mfa
```
7*. Проверить корпус
```commandline
mfa validate /путь/к/корпусу russian_mfa russian_mfa
```
8. Запустить mfa
```commandline
mfa align /путь/к/корпусу russian_mfa russian_mfa /путь/к/выходному/каталогу
```

## BFA
1. Сделать корпус в формате, как для mfa
2. Запустить скрипт предварительно поменяв путь до корпуса в скрипте ([скрипт](bfa/src/bfa.py))

Выходные данные будут на каталог выше в каталоге out

Также у bfa можно посмотреть [блокнот](bfa/src/bfa.ipynb)

## Датасеты
1. https://ruslan-corpus.github.io/
   А также [парсер](utils/ruslan_parser.py) для него. Это парсер берет csv файл, указанный в скрипте, делает папку out_lab и делает для каждой строчки .lab файл с транскрипцией. Формат каждой строки [название файла]|[транскрипция] и на выходе получаются файлы [название файла].lab с текстовой транскрипцией
