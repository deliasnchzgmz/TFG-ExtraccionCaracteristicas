
import os, os.path, natsort, cv2, xlsxwriter, openpyxl, time
import matplotlib.pyplot as plt
from skimage import io
import getimg



name = []
image = []
charact = ["image","name", "duration", "scale"]
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
    return image, name


def initWorksheet(wbname):
    workbook = xlsxwriter.Workbook(wbname+'.xlsx')
    worksheet = workbook.add_worksheet("mainsheet")
    
    worksheet.write('B'+str(1), charact[1])
    worksheet.write('D'+str(1), charact[2])
    worksheet.write('E'+str(1), charact[3])

    workbook.close()
    return workbook


def writeName(wbname):
    workbook = openpyxl.load_workbook(wbname+'.xlsx')

    currentSheet = workbook['mainsheet']
    i = 1
    for element in name:
        i = i+1
        currentSheet['A'+ str(i)].value = i-1
        currentSheet['B'+ str(i)].value = name[i-2]
    workbook.save(wbname+'.xlsx')
    return workbook

while(1):

    print("What do you want to do?")
    opt = int(input())

    switch(opt)
    print("Type the desired name for datasheet: ")
    wbname = input()
    wb = initWorksheet(wbname)
    print("Loading...")
    time.sleep(2)
    print("Datasheet generated!")
    time.sleep(1)
    print("Ready to add data!")
    time.sleep(1)
    print("Please introduce the name of the folder: ")
    data = databaseFeatures(input())
    print("Collecting data...")
    time.sleep(1)
    workbook = writeName(wbname)
    print("Saved data.")
    print(workbook)
    quit()









    







