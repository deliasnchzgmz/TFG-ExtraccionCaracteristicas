import cv2
import numpy as np
import utils, midi

mscore_img = cv2.imread('resources/sheets/p-1.png', cv2.IMREAD_UNCHANGED)

crotchet_temp = cv2.imread('resources/templates/crotchet_temp.png', cv2.IMREAD_UNCHANGED)
g_clef_temp = cv2.imread('resources/templates/g_clef.png', cv2.IMREAD_UNCHANGED)
minim_temp = cv2.imread('resources/templates/minim_temp.png', cv2.IMREAD_UNCHANGED)
c_temp = cv2.imread('resources/templates/c_temp.png', cv2.IMREAD_UNCHANGED)
stem_temp = cv2.imread('resources/templates/stem_temp.png', cv2.IMREAD_UNCHANGED)
crotchetR_temp = cv2.imread('resources/templates/cr_temp.png', cv2.IMREAD_UNCHANGED)
minimR_temp = cv2.imread('resources/templates/minim_rest_temp.png', cv2.IMREAD_UNCHANGED)
quaverR_temp = cv2.imread('resources/templates/quaverrest_temp.png', cv2.IMREAD_UNCHANGED)


mscore_img = cv2.cvtColor(mscore_img, cv2.COLOR_BGRA2BGR)
crotchet_temp = cv2.cvtColor(crotchet_temp, cv2.COLOR_BGRA2BGR)
g_clef_temp = cv2.cvtColor(g_clef_temp, cv2.COLOR_BGRA2BGR)
minim_temp = cv2.cvtColor(minim_temp, cv2.COLOR_BGRA2BGR)
c_temp = cv2.cvtColor(c_temp, cv2.COLOR_BGRA2BGR)
stem_temp = cv2.cvtColor(stem_temp, cv2.COLOR_BGRA2BGR)
crotchetR_temp = cv2.cvtColor(crotchetR_temp, cv2.COLOR_BGRA2BGR)
minimR_temp = cv2.cvtColor(minimR_temp, cv2.COLOR_BGRA2BGR)
quaverR_temp = cv2.cvtColor(quaverR_temp, cv2.COLOR_BGRA2BGR)

counter = np.zeros(mscore_img.shape[0]-1)
image_gray, bin_img  = utils.image_preprocessing(mscore_img,threshold = 200) # imagen binaria
line_pos = utils.lines_location(bin_img, counter)
staff_lines= utils.staffs(line_pos)
nolines_img = utils.detect_ei(bin_img, staff_lines)

l = []
cropped_img = []
cuts = [0]

for staff in range(len(staff_lines)-1):
    cuts.append(round((staff_lines[staff][10]+staff_lines[staff+1][10])/2))
cuts.append(mscore_img.shape[1])
for border in range(len(cuts)-1):
    cropped_img.append(mscore_img[cuts[border]:cuts[border+1]])
 
if len(cropped_img)>1:
    im_v = cv2.vconcat([cropped_img[0], cropped_img[1]])

cv2.imwrite('resources/out/output.png', mscore_img) 
#cv2.imshow('output', im_v)
#cv2.waitKey(0) 
#cv2.destroyAllWindows() 