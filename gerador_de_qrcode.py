import qrcode
from PIL import Image

# Dados que serão codificados no QR Code
ler_input = str(input("Digite o link para virar um QR CODE:\n>> "))
data = ler_input

# Gera o QR Code
img = qrcode.make(data)

# Salva a imagem do QR Code
img.save("qrcode_example.png")

# Abre a imagem do QR Code para visualização (opcional)
img.show()
