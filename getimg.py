import natsort, os, sys
from skimage import io
import matplotlib.pyplot as plt
import time



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

if( __name__ == '__main__'):
    databaseFeatures("img")
    n = 5
    while(1):
        print("which image do you want to plot?")
        num = input()
        print("you are printing image "+(num)+" which is called "+name[int(num)-1])
        plt.imshow(image[int(num)-1])
        plt.show()
        print("restart? [Y/N]")
        restart = input()
        if restart is not ("y" or "Y" or "n" or "N"):
            print("please type y or n")
            restart = input()
        if restart == "y" or "Y":
            print("restarting...")
            time.sleep(3)
        else:
             quit()

        

            

        


