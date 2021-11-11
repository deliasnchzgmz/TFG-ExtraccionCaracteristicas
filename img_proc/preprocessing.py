import os, math
import cv2
import numpy as np
from skimage.morphology import binary_dilation
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola

##En este script se pretende aplicar los procesados de imagen necesarios para
#implementar posteriormente los algoritmos de extracción de información a la imagen



def lines_location (image):
    # saco la imagen pentagrama e imagen sin pentagrama
    # y la localizacion de las lineas de pentagrama
    blank = image.copy()    
    blank.fill(255)
    no_lines = image.copy()
    line_pos = []   
    counter = np.zeros([image.shape[0]])
    #line_pos_init = []
    
    #numero de pixeles en negro que tiene cada linea
    #se almacena en un vector
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == 0:
                counter[i] = counter[i] + 1
    
    for i1 in range(len(counter)):
        if ((counter[i1]/len(image[i1]))>0.4):
            line_pos.append(i1)
            for j1 in range(len(image[i1])):
                if image[i1][j1] == 0:
                    no_lines[i1][j1] = 255
                    blank[i1][j1] = 0

    #blank = lines_proc(blank)

    '''# saco donde empiezan las lineas
    for i in range(len(line_pos)):
        for j in range(len(blank[i])):
            if blank[line_pos[i][j]]==0:
                line_pos_init.append(p)
                break
    # media de inicio de las líneas
    mean_lines_init = sum(line_pos_init)/len(line_pos_init)'''

    return blank, no_lines, line_pos

def no_lines_proc(no_lines):
    #aplico morfología: defino un kernel y dilato las zonas en negro (los elementos musicales)
    kernel1 = np.array([[1],[1],[1]])
    dilation = binary_dilation(cv2.bitwise_not(no_lines), kernel1).astype(np.uint8)*255
    dilation = cv2.bitwise_not(dilation)
    
    return dilation

def lines_proc(blank):
    kernel2 = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    blank = binary_dilation(cv2.bitwise_not(blank), kernel2).astype(np.uint8)*255
    blank = cv2.bitwise_not(blank)

    return blank



