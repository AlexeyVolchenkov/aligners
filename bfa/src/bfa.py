import time
from pathlib import Path
from bournemouth_aligner import PhonemeTimestampAligner

directory_path = "../../input/ruslan/audio_16khz"  # путь до корпуса

input_path = Path(directory_path)
output_dir = input_path.parent / "out"
output_dir.mkdir(parents=True, exist_ok=True)


bfa_aligner = PhonemeTimestampAligner(
    preset="ru",
    duration_max=10,
    device='auto'
)

wav_files = sorted(list(Path(directory_path).glob("*.wav")))

tStart = time.time()

for wav_path in wav_files:
    try:
        lab_path = wav_path.with_suffix('.lab')

        if not lab_path.exists():
            print(f"Не найден .lab файл для {wav_path.name}")
            continue

        with open(lab_path, 'r', encoding='utf-8') as f:
            text_sentence = f.read().strip()

        print(f"Обработка: {wav_path.name}")
        audio_wav = bfa_aligner.load_audio(str(wav_path))

        t0 = time.time()
        timestamps = bfa_aligner.process_sentence(
            text_sentence,
            audio_wav,
            extract_embeddings=False,
            do_groups=True,
            debug=True
        )
        t1 = time.time()

        print(f"  Время обработки: {t1 - t0:.2f} сек")

        textgrid_content = bfa_aligner.convert_to_textgrid(
            timestamps_dict=timestamps,
            output_file=None,
            include_confidence=False
        )

        output_file = output_dir / f"{wav_path.stem}.TextGrid"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(textgrid_content)

        print(f"  Сохранено: {output_file}")

        bfa_aligner.reset_counters()

    except Exception as e:
        print(f"Ошибка при обработке {wav_path.name}: {str(e)}")
        continue

tEnd = time.time()

print(f"Время обработки {len(wav_files)} файлов: {tEnd - tStart:.2f} сек")

