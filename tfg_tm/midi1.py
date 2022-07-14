import os, natsort, cv2

db = 'resources/sheets'
folders = natsort.natsorted(os.listdir(db))
imPaths = []
labels = []

for i,f in enumerate(folders):

    imPaths.extend( [ db+'/'+f+'/'+str(i+1)+'.png'] )
    #labels.extend( numImages*[(i+1)] )

