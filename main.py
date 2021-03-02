import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

# Abrindo arquivo da imagem
original_image = cv2.imread('input.jpg', 0)

# Obtendo propriedades da imagem
width,height = np.shape(original_image)

# Setando variaveis auxiliares
hist = np.full(256, 0)
total_pixels = 0
curr = 0


# Calculando histograma
for i in range(0, width):
    for j in range(0, height):
        col = original_image[i, j]
        hist[col] = hist[col] + 1

max_value = np.amax(hist) + 100

# Configurando Figuras 
fig = plt.figure(constrained_layout=True)

# Setando grades
gs = fig.add_gridspec(2, 2)
a0 = fig.add_subplot(gs[0, :])
a1 = fig.add_subplot(gs[-1, 0])
a2 = fig.add_subplot(gs[-1, 1])

# Plotando imagem original
a0.imshow(original_image, 'gray')
a0.set_title('Original Image')
a0.axis(False)

# Plotando histograma o implementado nesse script
a1.fill_between(np.arange(0, 255, 1), hist[:-1], 0, facecolor='green', alpha=0.5)
a1.set_title('Implemented Histogram')
a1.set_ylim(0, max_value)

# Plotando o histograma implementado pelo matplotlib
a2.hist(original_image.ravel(),256)
a2.set_title('MatPlotLib Histogram')

# Salvando output em arquivo
fig.savefig('output.jpg')

# Renderizando graficos em uma janela
plt.show()
