# import pytesseract
# import cv2

# def process_image(image_path):
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     blur = cv2.medianBlur(gray, 3)
#     _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789'
#     text = pytesseract.image_to_string(thresh, config=custom_config)
#     return text.strip()

import pytesseract
import cv2
import os

def process_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"Imagem não pode ser carregada: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Para debug (remover ou comentar depois)
    # cv2.imwrite("debug_thresh.png", thresh)

    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    return text.strip()
