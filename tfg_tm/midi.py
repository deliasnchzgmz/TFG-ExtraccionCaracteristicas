from midiutil.MidiFile import MIDIFile

def decode(element):
    
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72, 74, 78, 79]  # MIDI note number
    volume = 0
    duration = 0
    pitch = 0

    if element[1] == 'G CLEF' or element[1] == '4/4 TS':
        return
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
        

def generateMIDI(elements):
    mf = MIDIFile(1) #only 1 track
    
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    

    mf.addTempo(track, time, tempo)
    
    for i in range(1,len(elements)):
        volume, duration, pitch = decode(elements[i])
        
        time = time+duration
        mf.addNote(track, channel,  pitch, time, duration, volume)
    
        
    with open("resources/out/midifile.mid", "wb") as output_file:
        mf.writeFile(output_file)
        



