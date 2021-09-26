
import natsort, skimage, numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from skimage import io

image = []

image.append(io.imread('img/pantostao.png'))
plt.imshow(image[0])
plt.show()


