import cv2
import numpy as np
from PIL import Image

def image_preprocessing(image, threshold): # binariza la imagen y prepara para extraer las lineas y las figuras
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,bin_img = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY) # binariza la imagen: negro (0) o blanco (1)
   
    return image_gray, bin_img


def lines_location (bin_img, counter):
    line_pos = []
    delete_lines = []
    ##comprueba las líneas que tienen negro
    for i in range(len(bin_img)):
        for j in range(len(bin_img[i])):
            if bin_img[i][j]==0:
                counter[i] = counter[i] + 1
    #se queda con la posición de las líneas que tienen más de un X% de negro  
    for x in range(len(counter)):
        if (counter[x]/len(bin_img[x])>0.5):
            line_pos.append(x)    
    #borra las lineas duplicadas
    for duplicate in range(0,len(line_pos)-1):
        if line_pos[duplicate+1] == line_pos[duplicate]+1:
            delete_lines.append(duplicate)
    for delete in reversed(delete_lines):
        del line_pos[delete]

    return line_pos


def staffs(line_pos):
  st = []
  if (len(line_pos)%5 == 0):
    num_staffs = int(len(line_pos)/5)
    for group in range(0,num_staffs):
      diff = 0
      for space in range(1,len(line_pos)):
        diff = diff + (line_pos[space]-line_pos[space-1]) ##media de los espacios para colocar una línea al mismo espacio por debajo del pentagrama

      ##líneas del pentagrama
      st.append([int(line_pos[0+5*group]-diff/4), line_pos[0+5*group], line_pos[1+5*group], line_pos[2+5*group], line_pos[3+5*group], line_pos[4+5*group]])

      ##localización de los espacios del pentagrama
      st[group].insert(5,int((line_pos[3+5*group]+line_pos[4+5*group])/2))
      st[group].insert(4,int((line_pos[2+5*group]+line_pos[3+5*group])/2))
      st[group].insert(3,int((line_pos[1+5*group]+line_pos[2+5*group])/2))
      st[group].insert(2,int((line_pos[0+5*group]+line_pos[1+5*group])/2))
      st[group].insert(1,int((st[group][0]+line_pos[0+5*group])/2))
  return st

def detect_ei(bin_img, staff_lines):
    firstLine = staff_lines[0][2]
    lastLine = staff_lines[0][len(staff_lines[0])-1]
    staff_width = lastLine - firstLine
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    bin_img = cv2.bitwise_not(bin_img)
    bw = cv2.adaptiveThreshold(bin_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                               cv2.THRESH_BINARY, 15, -2)
    h = np.copy(bw)
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 10))
    horizontalStructureD = cv2.getStructuringElement(cv2.MORPH_RECT, (80, 1))
    h = cv2.erode(h, horizontalStructure)
    h = cv2.dilate(h, horizontalStructureD)


    h = cv2.bitwise_not(h)

    return h


def sortX(rect): ##ordenar las notas de derecha a izq
  if  (len(np.array(rect, object).shape)==2):
      r = rect[0][0][0]
  else:  r = rect[0]
  return r

def find_nearest(array, value):
  difference_array = np.absolute(array-value)
  index = difference_array.argmin()
  return index


def find_note(single_staff, rectY):
    notes = {
      10 : 'C',
      9 : 'D',
      8 : 'E',
      7 : 'F',
      6 : 'G',
      5 : 'A',
      4 : 'B',
      3 : 'c',
      2 : 'd',
      1 : 'e',
      0: 'f'
  }
    rect_note = notes[find_nearest(single_staff, rectY)]

    return rect_note   

  
def notes_per_staff(staff_lines, rect, h):
  notes_out = []
  out = []
  inside_staff = []
  number_staffs = len(staff_lines) ##cuántos pentagramas se han detectado?


  for p in range(0, number_staffs): ##para cada pentagrama
    for r in range(0, len(rect)):
      if rect[r][1]> staff_lines[p][0] and rect[r][1]< staff_lines[p][10]: ##si está dentro del pentagrama evaluado
        notes_out.append(rect[r])
    notes_out.sort(key=sortX)
    for r in range(0, len(notes_out)): ##me quedo con la y de cada una y le sumo h/2 para hallar la nota
      notes_out[r] = notes_out[r][1]-h/2
      out.append(find_note(staff_lines[p], notes_out[r]))  

  return notes_out, out


def get_rectangles_figures(mscore_img, template, staff_lines, threshold): ##Template matching y obtener rectángulos
    h = template.shape[0]
    w = template.shape[1]
    result = cv2.matchTemplate(mscore_img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    yloc, xloc = np.where(result>=threshold)
    
    rectangles = []
    rectangles_list = []
    for(x, y) in zip(xloc, yloc):
      rectangles.append([int(x), int(y), int(w), int(h)])
      rectangles.append([int(x), int(y), int(w), int(h)])
      
    if len(rectangles)>0:  
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        rectangles_list = rectangles.tolist()
    rectangles_list.sort(key=sortX)
    notes_out, out = notes_per_staff(staff_lines, rectangles, h)
    
    return rectangles_list, out


def get_rectangles_clef(mscore_img, template,  name):
    h = template.shape[0]
    w = template.shape[1]
    result = cv2.matchTemplate(mscore_img, template, cv2.TM_CCOEFF_NORMED)
    
    if name=='stem':
       flipped_stem = cv2.flip(template, 0) #vertical flip
       result_flipped = cv2.matchTemplate(mscore_img, flipped_stem, cv2.TM_CCOEFF_NORMED)
       result = result+result_flipped
       
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = 0.85
    yloc, xloc = np.where(result>=threshold)
    
    out = []
    rectangles = []
    rectangles_list = []
    
    for(x, y) in zip(xloc, yloc):
      rectangles.append([int(x), int(y), int(w), int(h)])
      rectangles.append([int(x), int(y), int(w), int(h)])
      
    if len(rectangles)>0:  
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        rectangles_list = rectangles.tolist()
        out = [name]
    

    
    return rectangles_list, out
    
    
def draw_rectangles(mscore_img, l):
    
    for i in range(len(l)):
        cv2.rectangle(mscore_img, (l[i][0][0], l[i][0][1]), (l[i][0][0]+l[i][0][2], l[i][0][1]+l[i][0][3]), (255, 0, 0), 2)
        if len(l[i])>2:
            cv2.putText(mscore_img, l[i][2], (l[i][0][0], l[i][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        else: cv2.putText(mscore_img, l[i][1], (l[i][0][0], l[i][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


def order_lists(clef, clef_out, c, c_out, crotchet, crotchet_out, minim, minim_out, quaver, quaver_out, crotchetR, minimR, minimR_out, quaverR, quaverR_out):
    full_list = []
    full_list.append([clef[0], clef_out[0]])
    for i in range(len(c)):
        full_list.append([c[i], c_out[i]])
    for i in range(len(crotchet)):
        full_list.append([crotchet[i], '', crotchet_out[i]])
    for i in range(len(minim)):
        full_list.append([minim[i], '2', minim_out[i]])
    for i in range(len(crotchetR)):
        full_list.append([crotchetR[i], 'z'])
    for i in range(len(quaver)):
        full_list.append([quaver[i], '/2', quaver_out[i]])
    for i in range(len(quaverR)):
        full_list.append([quaverR[i], 'z/2'])
    for i in range(len(minimR)):
        if minimR_out[i] == 'SI':
            full_list.append([minimR[i], 'z4'])
        else: full_list.append([minimR[i], 'z2'])
    
    full_list.sort(key=sortX)
    return full_list


def detect_quaver(crotchet, crotchet_out, quaver_stem, nolines_img):
    quaver_list = []
    quaver_out = []
    delete = []
    ndelete = []
    loc = []
    for stem in range(len(quaver_stem)):
        s = []
        s.extend(range(quaver_stem[stem][0]-23,(quaver_stem[stem][0]+quaver_stem[stem][2])))
        loc.append(s)
        
    for line in range(nolines_img.shape[0]):
        a = np.where(nolines_img[line]==0)
        if (len(a[0]))>1:
            loc.append(a[0])
    loc = [loc for sub in loc for loc in sub]
    for line in range(len(quaver_stem)):
        quaver_stem[line][0]

    if(len(loc)>0):
        for c in reversed(range(0,len(crotchet))):
            for l in range(len(loc)):
                if(loc[l] and crotchet[c][0]==loc[l]):
                   delete.append(c)  
        for element in delete:
            if element not in ndelete:
                ndelete.append(element)
        for d in (range(len(ndelete))):
            quaver_list.append(crotchet.pop(ndelete[d]))
            quaver_out.append(crotchet_out.pop(ndelete[d]))

    return crotchet, crotchet_out, quaver_list[::-1], quaver_out[::-1]

            
def concatenate(cropped_img):
    if len(cropped_img)<2: 
        return cropped_img[0]
    else: 
        return cv2.vconcat([cv2.hconcat(cropped_img) for list_h in cropped_img])

def cv_to_pil(image):
    blue,green,red = cv2.split(image)
    image = cv2.merge((red,green,blue))
    im = Image.fromarray(image)
    return im