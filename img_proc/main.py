##En este script pretendo importar la imagen y procesarla para poder extraer la informacion musical correspondiente
import os, math
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io
from skimage.morphology import binary_dilation




image = []
image.append(io.imread('part_hb.jpg'))
#plt.imshow(image[0])
#plt.show()

line_pos = []
line_pos_init = []
c = 0

gray_img = cv2.cvtColor(image[0], cv2.COLOR_BGR2GRAY)
_,bin_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
test = bin_img.copy()
blank = test.copy()

plt.imshow(test, cmap='gray')
plt.show()

height, width = bin_img.shape
counter = np.zeros([height])


##comprueba las líneas que tienen negro
for i in range(len(test)):
    for j in range(len(test[i])):
        if bin_img[i][j]==0:
            counter[i] = counter[i] + 1
            #blank[i][j] = 255
   
#se queda con la posición de las líneas que tienen más de un 65% de negro  
# saco la imagen sin partituras y la imagen partituras
          
for x in range(len(counter)):
    if (counter[x]/len(counter)>0.65):
        line_pos.append(x)
        for b in range(len(test[x])):
            if test[x][b] == 0:
                test[x][b] = 255
                blank[x][b] = 0

for pos in range(len(line_pos)):
    for p in range(len(blank[1])):
        if blank[line_pos[pos]][p]==0:
            line_pos_init.append(p)
            break
mean_lines_init = sum(line_pos_init)/len(line_pos_init)
    
print('esta es la imagen sin partituras')

plt.imshow(test, cmap='gray')
plt.show()


print('esta es la imagen en blanco')

plt.imshow(blank, cmap='gray')
plt.show()
cv2.imwrite('sinpart.png',test)
#plt.imshow(test1, cmap='gray')
#plt.show()
#488, 262

#Ahora voy a trabajar con la imagen sin pentagramas: primero dilato y luego erosiono para 
# pintar los huecos que deberian tener linea
#esto se llamaba: CIERRE

kernel = np.array([[1],[1],[1],[1]])
closing = binary_dilation(cv2.bitwise_not(test), kernel).astype(np.uint8)*255
closing = cv2.bitwise_not(closing)

cv2.imwrite('closing.png',closing)
plt.imshow(closing, 'gray')
plt.show()