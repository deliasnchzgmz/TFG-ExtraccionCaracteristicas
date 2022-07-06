# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:48:22 2022

@author: dl2pa
"""

#!/usr/bin/env python

from midiutil import MIDIFile
import main as m

figures = []

degrees  = [60, 62, 64, 65, 67, 69, 71, 72, 74, 78, 79]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

elements = m.l


def decode(element):
    
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72, 74, 78, 79]  # MIDI note number
    volume = 0
    duration = 0
    pitch = 0

    if element[1] == 'G CLEF' or element[1] == '4/4 TS':
        volume = 0
        duration = 0
        pitch = 0
    if (element[1]=='crotchet') or (element[1]=='minim') or (element[1]=='quaver'):
        volume = 100
        if (element[1]=='crotchet'): 
            duration = 1 
            
        if (element[1]=='minim'): 
            duration = 2 

        if (element[1]=='quaver'): 
            duration = 0.5 
        
        if (element[2]=='DO'): 
            pitch = degrees[0] 

        if (element[2]=='RE'): 
            pitch = degrees[1] 

        if (element[2]=='MI'): 
            pitch = degrees[2] 

        if (element[2]=='FA'): 
            pitch = degrees[3] 

        if (element[2]=='SOL'): 
            pitch = degrees[4] 

        if (element[2]=='LA'): 
            pitch = degrees[5] 

        if (element[2]=='SI'): 
            pitch = degrees[6] 

        if (element[2]=='DO*'): 
            pitch = degrees[7] 

        if (element[2]=='RE*'): 
            pitch = degrees[8] 

        if (element[2]=='MI*'): 
            pitch = degrees[9] 

        if (element[2]=='FA*'): 
            pitch = degrees[10]

        
    if (element[1]=='crotchet rest') or (element[1]=='minim rest') or (element[1]=='quaver rest'):
        volume = 0
        pitch = degrees[0]
        if (element[1]=='crotchet rest'): 
            duration = 1 

        if (element[1]=='minim rest'): 
            duration = 2 

        if (element[1]=='quaver rest'): 
            duration = 0.5 
          
    
    return volume, duration, pitch




for i in range(2,len(elements)):
    volume, duration, pitch = decode(elements[i])
    time = time+duration
    figures.append([track, channel,  pitch, time, duration, volume])
'''


for i, pitch in enumerate(degrees):
    time = time + duration
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    duration=duration+1

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
'''