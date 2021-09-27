import time
import functions as f

n=5

def program():
    print("Type the desired name for datasheet: ")
    wbname = input()
    wb = f.initWorksheet(wbname)
    print("Loading...")
    time.sleep(2)
    print("Datasheet generated!")
    time.sleep(1)
    print("Ready to add data!")
    time.sleep(1)
    print("Please introduce the name of the folder: ")
    data = f.databaseFeatures(input())
    print("Collecting data...")
    time.sleep(1)
    workbook = f.writeName(wbname)
    print("Saved data.")
    n=5
    

def error():
    print("There has been an error.")
    print("Exiting the program...")



print("What do you want to do?")
opt = int(input())

switch = {
    1 : program(),
    2 : quit()
}

while(n>0):
    switch.get(opt,error)
    continue


#C:\Users\dl2pa\OneDrive\Imágenes\flechas.png




    









    







