import preprocessing
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image = io.imread('part_hb.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
blank, no_lines, line_pos = preprocessing.lines_location(image)
dilation = preprocessing.no_lines_proc(no_lines)

'''
plt.imshow(image, 'gray')
plt.show()
plt.imshow(blank, 'gray')
plt.show()
plt.imshow(no_lines, 'gray')
plt.show()
plt.imshow(dilation, 'gray')
plt.show()
'''