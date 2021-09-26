import xlsxwriter
from PIL import Image
import os, os.path, natsort, cv2
import matplotlib.pyplot as plt
from skimage import io


name = []
image = []
data = [image, name]

def databaseFeatures(db):
    folder = natsort.natsorted(os.listdir(db))
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in folder:
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        name.append(f.partition('.')[0])
        image.append(io.imread(db+"/"+(f)))
    return 0

databaseFeatures("img")
workbook = xlsxwriter.Workbook('script.xlsx')
worksheet = workbook.add_worksheet()

i = 1
a = 0
for element in name:
    i = i+1
    worksheet.write('A'+str(i), (data[1])[i-2])

    
workbook.close()
