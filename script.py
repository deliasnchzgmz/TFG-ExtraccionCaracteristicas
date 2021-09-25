import xlsxwriter
from PIL import Image
import os, os.path, natsort, cv2
import matplotlib.pyplot as plt
from skimage import io


imgs = []
folderpath = "img"
name = []
duration = {}
valid_images = [".jpg",".gif",".png",".tga"]
caracteristics = {'name': name, 'duration' : duration}
for f in os.listdir(folderpath):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(cv2.imread(os.path.join(folderpath,f)))
    name.append(f.partition('.')[0])

#print(name)
#plt.plot(imgs)
#print(img_path)

workbook = xlsxwriter.Workbook('script.xlsx')
worksheet = workbook.add_worksheet()

i = 1
a = 0
for element in name:
    i = i+1
    worksheet.write('A'+str(i), name[i-2])
    
workbook.close()
