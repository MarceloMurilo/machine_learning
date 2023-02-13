import cv2
from PIL import Image

# Carrega a imagem colorida
img = Image.open("lena/lena.jpg")

# Converte a imagem para níveis de cinza
gray_img = img.convert("L")

# Converte a imagem para binarização
binary_img = gray_img.point(lambda x: 0 if x < 128 else 255, "1")

# Salva as imagens convertidas
gray_img.save("imagem_cinza.jpg")
binary_img.save("imagem_binarizada.jpg")
