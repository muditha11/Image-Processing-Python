import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import os

image_file = "Resources/ocr.PNG"
img = Image.open(image_file)

ocr_result = pytesseract.image_to_string(img)

print(ocr_result)