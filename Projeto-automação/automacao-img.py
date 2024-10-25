import pytesseract
import cv2 as cv
from pdf2image import convert_from_path


# Ler a imagem (opencv)

imagem = cv.imread("images.jpeg")

caminho = r"C:\Program Files\Tesseract-OCR"


# extrair o texto da imagem (pytesseract)
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)

print(texto)
