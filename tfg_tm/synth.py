from music21 import *

'''f5 = note.Note("F5")
f = note.Note("F5")
c4 = note.Note("C4")
stream = stream.Stream()
stream.append(f5)
stream.append(c4)
stream.append(f)

stream.show('midi')
stream.write('midi', fp='resources/out/output.mid')'''

f = open("resources/out/demofile3.abc", "w")
f.write("X:1\nT:Tusa\nL:1/4\nQ: 1/4=170\nR:jig\nK:C\n")
f.write("d B A G z G/2 z/2  d B A G z G/2 z/2 c4")
f.close()

abcScore = converter.parse('resources/out//demofile3.abc')

abcScore.show('midi')
abcScore.write('midi', fp='resources/out/output.mid')