from PIL import Image
from pytesseract import pytesseract

img1=Image.open(r'C:\Users\anand\Downloads\Screenshot_Sep.PNG')
img2=Image.open(r'C:\Users\anand\Downloads\Screenshot_Oct.PNG')

pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text1=pytesseract.image_to_string(img1)
text2=pytesseract.image_to_string(img2)
text=text1+text2

