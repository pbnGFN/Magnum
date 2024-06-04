import numpy as np
import cv2 
from matplotlib import pyplot as plt

def get_center(filepath:str)->tuple:
    #read image in grayscale
    im = cv2.imread(filepath,0)

    #generate canny edges for the image
    canny = cv2.Canny(im,100,200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    print(len(contours), im.shape)
    #draw the largest contour
    blank = np.zeros(im.shape, dtype='uint8')
    cv2.drawContours(blank,contours,-1,(255,0,0),1)
    cv2.imwrite(r'images/all_arcs.png', blank)

    max_contours = sorted(contours, key=lambda c: cv2.arcLength(c, True), reverse=True)
    select, next_select  =  max_contours[0:2]
    blank = np.zeros(im.shape, np.uint8)
    blank.shape
    cv2.fillPoly(blank, pts=select, color= (255,0,0))
    save_path = r'images/largest_arc.png'
    cv2.imwrite(save_path,blank)
    #GRAB THE CENTROID
    M = cv2.moments(select)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    #return the centroid
    return (cx,cy,save_path)