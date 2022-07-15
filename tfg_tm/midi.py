from music21 import *

def write_midi(l, file, output):
    
    f = open(file, "w")
    f.write("X:1\nT:Tusa\nL:1/4\nQ: 1/4=100\nR:jig\nK:C\n")
    
    for el in l:
        if "CLAVE" in el[1] or "TS" in el[1]:
            continue
        else:
            if len(el)>2:
                f.write(el[2]+el[1] +" ")
            else:
                f.write(el[1] + " ")
            
    f.close()
    abcScore = converter.parse(file)

    #bcScore.show('midi')
    abcScore.write('midi', fp = output)

