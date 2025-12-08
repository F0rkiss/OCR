import os
import cv2
import numpy as np
from paddleocr import PaddleOCR

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ocr_id = PaddleOCR(use_angle_cls=True, lang='id')
ocr_en = PaddleOCR(use_angle_cls=True, lang='en')

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    img_path = os.path.join(INPUT_DIR, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f"❌ Failed to load {filename}")
        continue

    print(f"✅ Image loaded: {filename} {img.shape}")

    # OCR
    res_id = ocr_id.ocr(img, cls=True)
    res_en = ocr_en.ocr(img, cls=True)

    print("ID OCR done")
    print("EN OCR done")

    # Save text result
    output_txt = os.path.join(OUTPUT_DIR, filename + ".txt")
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("=== OCR ID ===\n")
        for line in res_id[0]:
            f.write(f"{line[1][0]}\n")

        f.write("\n=== OCR EN ===\n")
        for line in res_en[0]:
            f.write(f"{line[1][0]}\n")

    print(f"✅ Saved OCR result: {output_txt}")
