from music21 import *

def write_midi(l, file, output):

    n = {
      'C':'DO',
      'D':'RE',
      'E':'MI',
      'F':'FA',
      'G':'SOL',
      'A':'LA',
      'B':'SI',
      'c':'DO*',
      'd':'RE*',
      'e':'MI*',
      'f':'FA*'
  }
    figure = {
        '':'negra',
        '2':'blanca',
        '/2':'corchea',
        'z':'silencio de negra',
        'z2':'silencio de blanca',
        'z/2':'silencio de corchea'
    }

    alt = ''
    f = open(file, "w")

    check = False
    sharp_count = 0
    flat_count = 0
    for el in l:
        if "CLAVE" in el[1] or "TS" in el[1]:
            if "CLAVE" in el[1]: check = True
            if "TS" in el[1]: check = False
            
        else:
            if check==True:
                if "SOSTENIDO" in el[1]: sharp_count = sharp_count+1
                else: 
                    if "BEMOL" in el[1]: flat_count = flat_count+1
    

    t = open("resources/out/caracteristicas.txt", "w")
    t.write("Clave de Sol (en segunda línea)\n")
    t.write("Tonalidad: ")
    if sharp_count==0 and flat_count==0: 
        tonal="DO MAYOR"
        ab = "C"
    if sharp_count==1: 
        tonal="SOL MAYOR"
        ab = "G"
    if sharp_count==2: 
        tonal="RE MAYOR"
        ab = "E"
    if sharp_count==3: 
        tonal="LA MAYOR"
        ab = "A"
    if sharp_count==4: 
        tonal="MI MAYOR"
        ab = "D"
    if sharp_count==5 or flat_count==7: 
        tonal="SI MAYOR"
        ab = "B"
    if sharp_count==6 or flat_count==6: 
        tonal="FA# MAYOR / SOLb MAYOR"
        ab = "F#"
    if sharp_count==7 or flat_count==5: 
        tonal="REb MAYOR"
        ab = "Eb"
    if flat_count==4: 
        tonal="LAb MAYOR"
        ab = "Ab"
    if flat_count==3: 
        tonal="MIb MAYOR"
        ab = "Db"
    if flat_count==2: 
        tonal="SIb MAYOR"
        ab = "Bb"
    if flat_count==1: 
        tonal="FA MAYOR"
        ab = "F"
 
    t.write(tonal+"\n")
    t.write("Lista de figuras: \n")

    f.write("X:1\nT:Title\nL:1/4\nQ: 1/4=100\nR:jig\nK:"+ab+"\n")
        
    for el in l:
        if len(el)>2:
            f.write(el[2]+el[1])
            if alt=='':
                t.write('\t'+n[el[2]]+' '+figure[el[1]]+'\n')
            else:
                t.write('\t'+n[el[2]]+' '+alt+' '+figure[el[1]]+'\n')
                alt=''
        else:
            if "CLAVE" in el[1] or "TS" in el[1]:
                if "CLAVE" in el[1]: check = True
                if "TS" in el[1]: check = False
            if "SOSTENIDO" in el[1] and check==False: 
                f.write("^")
                alt = el[1]
            else: 
                if "BEMOL" in el[1] and check==False: 
                    f.write("_")
                    alt=el[1]
                else: 
                    if "BECUADRO" in el[1]: 
                        f.write("=")
                        alt="NATURAL"
                    else: 
                        if "z" in el[1]: 
                            f.write(el[1])
                            if alt=='':
                                t.write('\t'+figure[el[1]]+'\n')


    
    f.close()
    t.close()
    abcScore = converter.parse(file)
    abcScore.write('midi', fp = output)

