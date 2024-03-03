import PyPDF2 as pdf

from PyPDF2 import PdfReader, PdfWriter

def get_text(pdf_path):
    file = open(pdf_path, "rb")
    reader = PdfReader(file)
    total_text = ""
    for i in range(0, len(reader.pages)):
        total_text = total_text + reader.pages[i].extract_text()
    print(total_text)

def main():
    file = input("What is file name? ")
    text = get_text(file)
    print(text)
   
main()

