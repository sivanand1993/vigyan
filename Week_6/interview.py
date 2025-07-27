from PIL import Image
from pytesseract import pytesseract

img=Image.open(r'C:\Users\anand\Downloads\Screenshot_Sep.PNG')

pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text=pytesseract.image_to_string(img)

print(text)