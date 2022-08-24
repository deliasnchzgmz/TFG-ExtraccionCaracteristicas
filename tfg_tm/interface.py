from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import utils, analysis, os, natsort, cv2, pygame

root = Tk()
root.title("TFG-EXTRACCIÓN DE LA INFORMACIÓN MUSICAL PRESENTE EN PARTITURAS EN FORMATO IMAGEN")
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

image_number = 0
label = Label(root, image=imList[image_number])
label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)

def forward(image_number, imList):
    global label
    global button_back
    global button_forward
    global button_analyze
    global status

    if image_number==len(imList): 
        button_forward = Button(root, text=">>", command=lambda: forward(image_number, imList), padx=200, pady=10, state=DISABLED)
    else:
        label.grid_forget()
        label = Label(image=imList[image_number])
        button_forward.grid_forget()
        button_back.grid_forget()
        button_analyze.grid_forget()
        status = Label(root, text="Imagen "+ str(image_number+1) +" de "+ str(len(imList)), bd=1, relief=SUNKEN, anchor=CENTER)
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1, imList), padx=200, pady=10)
        button_back = Button(root, text="<<", command=lambda: back(image_number-1, imList), padx=200, pady=10)   
        button_analyze = Button(root, text="Analizar", command = lambda: analizar(image_number), padx=200, pady=10)
        label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)
        status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)
        button_back.grid(row=2, column=0, padx= 100, pady=20)
        button_analyze.grid(row=2, column=1, padx= 100, pady=20)
        button_forward.grid(row=2, column=2, padx= 100, pady=20)
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
                pygame.mixer.music.stop()
                

def back(image_number, imList):
    global label
    global button_back
    global button_forward
    global button_analyze
    global status

    if image_number<0: 
        button_back = Button(root, text="<<", command=lambda: back(0, imList), padx=200, pady=10, state=DISABLED)    
    else:
        label.grid_forget()
        label = Label(image=imList[image_number])
        button_forward.grid_forget()
        button_back.grid_forget()
        button_analyze.grid_forget()
        status = Label(root, text="Imagen "+ str(image_number+1) +" de "+ str(len(imList)), bd=1, relief=SUNKEN, anchor=CENTER)
        button_back = Button(root, text="<<", command=lambda: back(image_number-1, imList), padx=200, pady=10)
        button_forward = Button(root, text=">>", command=lambda: forward(image_number+1, imList), padx=200, pady=10)
        button_analyze = Button(root, text="Analizar", command = lambda: analizar(image_number), padx=200, pady=10)
        label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)
        status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)
        button_back.grid(row=2, column=0, padx= 100, pady=20)
        button_analyze.grid(row=2, column=1, padx= 100, pady=20)
        button_forward.grid(row=2, column=2, padx= 100, pady=20)
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
                pygame.mixer.music.stop()

def analizar(image_number):
    global label
    global root
    global button_analyze

    image = utils.cv_to_pil(analysis.analysis(images[image_number]))
    label.grid_forget()
    button_analyze.grid_forget()
    image = image.resize((round(image.size[0]/round(image.size[1]/719)), round(image.size[1]/round(image.size[1]/719))))
    image = ImageTk.PhotoImage(image)
    label = Label(root, image = image)
    label.photo = image
    label.grid(row=0, column=0, columnspan=3, padx=w/5, pady=5, sticky=NS)
    button_analyze = Button(root, text="Características", command = lambda: play(), padx=200, pady=10)
    button_analyze.grid(row=2, column=1, padx= 100, pady=20)

    
def play():

    top = Toplevel()
    top.title("Características")
    top.iconbitmap('resources\icono.ico')
    top.geometry('500x400')

    txtarea = Text(top, width=40, height=20)
    txtarea.pack(pady=10)

    ch = open("resources/out/caracteristicas.txt", "r")  
    data = ch.read()
    txtarea.insert(END, data)
    ch.close()

    pygame.mixer.init()

    def music():
        pygame.mixer.music.load("resources/out/demofile.mid")
        pygame.mixer.music.play(loops=0)
    
    def stop_music():
        pygame.mixer.music.stop()

    controls_frame = Frame(top)
    controls_frame.pack(pady=10)

    stop_button = Button(controls_frame, text="Stop", command=stop_music, padx=20, pady=4)
    play_button = Button(controls_frame, text="Play", command=music, padx=20, pady=4)

    stop_button.grid(row=0, column=0)
    play_button.grid(row=0, column=1)
    

button_back = Button(root, text="<<", command=lambda: back(image_number-1, imList), padx=200, pady=10)
button_analyze = Button(root, text="Analizar", command = lambda: analizar(image_number), padx=200, pady=10)
button_forward = Button(root, text=">>", command=lambda: forward(image_number+1, imList), padx=200, pady=10)

button_back.grid(row=2, column=0, padx= 100, pady=20)
button_analyze.grid(row=2, column=1, padx= 100, pady=20)
button_forward.grid(row=2, column=2, padx= 100, pady=20)
status.grid(row=1, column=0, columnspan=3, pady=20, sticky=W+E)




root.mainloop()


