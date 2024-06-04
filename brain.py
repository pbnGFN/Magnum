import math
import magnum_opus
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt
import utils
import instruction

def test():
    b_x, b_y, t_x, t_y, c_x, c_y, save_path = magnum_opus.test()
    dx = t_x - b_x
    dy = (160-t_y) - (160-b_y)

    slope_character  = math.degrees(math.atan2(dy, dx))
    slope_character = slope_character if slope_character>=0 else slope_character + 360

    dx = c_x - b_x
    dy = (160-c_y) - (160-b_y)

    slope_path  = math.degrees(math.atan2(dy, dx))
    slope_path = slope_path if slope_path>=0 else slope_path + 360 

    
    print(abs(slope_path-slope_character), slope_character)
    if abs(slope_character - slope_path) < 23:
        instruction.move()

    else:
        instruction.rotate()
            

    img = Image.open(save_path)

    
    img = np.array(img)
    cv2.line(img, np.int_([b_x,b_y]), (c_x, c_y), color=(255,255,255), thickness=1)
    cv2.line(img, np.int_([b_x,b_y]), np.int_([t_x,t_y]), color=(255,255,255), thickness=1)
    cv2.imwrite(r'images\slope_plot.png',img)
    

