import natsort, os
from skimage import io
import matplotlib.pyplot as plt


def databaseFeatures(db="img"):
    folder = natsort.natsorted(os.listdir(db))
    valid_images = [".jpg",".gif",".png",".tga"]
    name = []
    img = []
    for f in folder:
        print(f)
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        name.append(f.partition('.')[0])
        #img.append(io.imread(db+"/"+(f)))
        image = io.imread(db+"/"+f)
    return image
print(folder)
(databaseFeatures("img")[0])

