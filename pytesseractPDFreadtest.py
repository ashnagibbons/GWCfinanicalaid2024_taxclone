import pytesseract
import PIL.Image
import cv2
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
    )

fname = "1040.pdf"
pil_image_lst = convert_from_path(fname, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
pil_image = pil_image_lst[0]


myconfig = r"--psm 12 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open(fname), config=myconfig)
print(text)
