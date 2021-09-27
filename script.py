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

def exitProgram():
    value = input("Do you want to exit? [Y/N]")
    while( (value=="y" or value=="Y" or value=="n" or value=="N") is False):
        print()
        value = input("Please type Y or N:")
    if (value=="Y" or value=="y"):
        quit()

print("What do you want to do?")
while(True):
    print("Type 1 to run the program.\nType 2 to add another image to data.\nType 3 to exit the program.")
    opt = int(input())
    if opt == 1:
        print("Executing program...")
        program()
        exitProgram()
    if opt == 2:
        print("Typed 2.")
    if opt == 3:
        quit()
        exitProgram()
    if (opt==1 or opt==2 or opt==3) is False:
        print("Please introduce a valid input.")


##





    









    







