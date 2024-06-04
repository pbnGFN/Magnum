import cv2
import numpy as np
import torch
from window_capture import WindowCapture
import crop_cut
import pos_orient
import segmentation
import get_centroid

def test():
    cap = WindowCapture()
    output_path = cap.get_screenshot()
    print(output_path + " Here")
    crop_wts = r'crop_wts\best.pt'
    map_path = crop_cut.crop_the_map(crop_wts,output_path)

    b_x, b_y, t_x, t_y , bbox = pos_orient.get_coordinates(r'detection_wts\last.pt', map_path)

    segment_path = segmentation.segment(r'seg_wts\checkpoint.pt',map_path)

    c_x, c_y, save_path = get_centroid.get_center(segment_path)
    return b_x, b_y, t_x, t_y, c_x, c_y, save_path





