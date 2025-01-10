import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("image_teste.png")

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

_, imagem_pb = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)


plt.figure(figsize=(10, 5))


plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Escala de Cinza")
plt.imshow(imagem_cinza, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Preto e Branco")
plt.imshow(imagem_pb, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
