#crop single image map and save it in result_crop.jpg [this is for a single image]
from ultralytics import YOLO
import cv2
import numpy as np
import os
import glob
import torch

import time
#used to crop the map

def crop_the_map(model_wt:str, screenshot_path:str)->str:
    model  = YOLO(r'crop_wts\best.pt')
    results = model.predict(screenshot_path)

    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        print(boxes.xywh)
        if(np.size(boxes.xywh.squeeze(0).cpu().numpy())==4):
            x, y , w, h = boxes.xywh.squeeze(0).cpu().numpy()
            x_start = int(np.round_(x - (w/2)))
            y_start = int(np.round_(y - (h/2)))
            x_end = int(np.round_(x_start + w))
            y_end = int(np.round_(y_start + h))
            print(x,y,w,h)
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            #result.show()  # display to screen
            result.save(filename=r'images\result.jpg')
            crop_img = cv2.imread(r'images\result.jpg')[y_start:y_end, x_start:x_end]
            
            cv2.imwrite(r'images\result_crop.jpg',crop_img)
    return r'images\result_crop.jpg'
