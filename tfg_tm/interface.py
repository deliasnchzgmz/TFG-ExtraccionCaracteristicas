from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import utils, os, natsort, cv2

root = Tk()
root.title("TFG DELI")
root.iconbitmap('resources\icono.ico')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

db = 'resources/sheets'
imList = []
images = natsort.natsorted(os.listdir(db))

for i,f in enumerate(images):
    image = Image.open(db+'/'+f)
    image = image.resize((round(image.size[0]/round(image.size[1]/719)), round(image.size[1]/round(image.size[1]/719))))
    imList.append(ImageTk.PhotoImage(image))

status = Label(root, text="Imagen 1 de "+ str(len(imList)), bd=1, relief=SUNKEN, anchor=CENTER)

label = Label(image=imList[0])
label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)

def forward(image_number, imList):
    global label
    global button_back
    global button_forward
    global status

    if image_number==len(imList): 
        button_forward = Button(root, text=">>", command=lambda: forward(0, imList), padx=200, pady=10, state=DISABLED)
    else:
        label.grid_forget()
        label = Label(image=imList[image_number])
        button_forward.grid_forget()
        status = Label(root, text="Imagen "+ str(image_number+1) +" de "+ str(len(imList)), bd=1, relief=SUNKEN, anchor=CENTER)
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1, imList), padx=200, pady=10)
        button_back = Button(root, text="<<", command=lambda: back(image_number-1, imList), padx=200, pady=10)   
        label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)
        status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)
        button_back.grid(row=2, column=0, padx= 100, pady=20)
        button_forward.grid(row=2, column=2, padx= 100, pady=20)
        


def back(image_number, imList):
    global label
    global button_back
    global button_forward
    global status
    if image_number<0: 
        button_back = Button(root, text="<<", command=lambda: back(0, imList), padx=200, pady=10, state=DISABLED)    
    else:
        label.grid_forget()
        label = Label(image=imList[image_number])
        button_forward.grid_forget()
        button_back.grid_forget()
        status = Label(root, text="Imagen "+ str(image_number+1) +" de "+ str(len(imList)), bd=1, relief=SUNKEN, anchor=CENTER)
        button_back = Button(root, text="<<", command=lambda: back(image_number-1, imList), padx=200, pady=10)
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1, imList), padx=200, pady=10)
        label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)
        status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)
        button_back.grid(row=2, column=0, padx= 100, pady=20)
        button_forward.grid(row=2, column=2, padx= 100, pady=20)

def play():
    top = Toplevel()
    top.title("New window")
    top.iconbitmap('resources\icono.ico')


button_back = Button(root, text="<<", command=lambda: back(0, imList), padx=200, pady=10)
button_quit = Button(root, text="Analizar", command = lambda: play(), padx=200, pady=10)
button_forward = Button(root, text=">>", command=lambda: forward(0, imList), padx=200, pady=10)

button_back.grid(row=2, column=0, padx= 100, pady=20)
button_quit.grid(row=2, column=1, padx= 100, pady=20)
button_forward.grid(row=2, column=2, padx= 100, pady=20)
status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)


root.mainloop()


