import os
from paddleocr import PaddleOCR

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    show_log=True
)

print("✅ PaddleOCR Loaded")

for fname in os.listdir(INPUT_DIR):
    if not fname.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    img_path = os.path.join(INPUT_DIR, fname)
    print(f"✅ Processing {fname}")

    result = ocr.ocr(img_path, cls=True)

    out_file = os.path.join(OUTPUT_DIR, fname + ".txt")
    with open(out_file, "w", encoding="utf-8") as f:
        for line in result[0]:
            text = line[1][0]
            conf = line[1][1]
            f.write(f"{text}\t{conf:.2f}\n")

    print(f"✅ Saved → {out_file}")

print("✅ All OCR done")
