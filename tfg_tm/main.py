import cv2
import numpy as np
import utils

mscore_img = cv2.imread('resources/sheets/nose-1.png', cv2.IMREAD_UNCHANGED)

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

cv2.imshow('output', nolines_img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 


crotchet_list, crotchet_out = utils.get_rectangles_figures(mscore_img, crotchet_temp, staff_lines, 0.7)
minim_list, minim_out = utils.get_rectangles_figures(mscore_img, minim_temp, staff_lines, 0.7)
clef_list, clef_out = utils.get_rectangles_clef(mscore_img, g_clef_temp, 'G CLEF')
c_list, c_out = utils.get_rectangles_clef(mscore_img, c_temp, '4/4 TS')
crotchetR_list, crotchetR_out = utils.get_rectangles_clef(mscore_img, crotchetR_temp, 'CROTCHET REST')
minimR_list, minimR_out = utils.get_rectangles_figures(mscore_img, minimR_temp, staff_lines, 0.9)
quaver_stem, _ = utils.get_rectangles_clef(mscore_img, stem_temp, 'stem')
quaverR_list, quaverR_out = utils.get_rectangles_clef(mscore_img, quaverR_temp, 'QUAVER REST')
crotchet_list, crotchet_out, quaver_list, quaver_out = utils.detect_quaver(crotchet_list, crotchet_out, quaver_stem, nolines_img)
l = utils.order_lists(clef_list, clef_out, c_list, c_out, crotchet_list, crotchet_out, minim_list, minim_out, quaver_list, quaver_out, crotchetR_list, minimR_list, minimR_out, quaverR_list, quaverR_out)
utils.draw_rectangles(mscore_img, l)


cv2.imwrite('resources/out/output.png', mscore_img) 
#midi.generateMIDI(l)
cv2.imshow('output', mscore_img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

