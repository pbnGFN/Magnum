from PIL import Image
from ultralytics import YOLO
import torch

def get_coordinates(wt_path:str, filename:str)->tuple:
    #grab image 
    im = Image.open(filename)
    im_resized = im.resize((160,160))
    
    
    #use yolo to grab results of orientation
    model = YOLO(wt_path)
    results = model(im_resized)
    results[0].save(r'images\delete.png')
    var = results[0]

    #grab keypoint coordinates
    bottom_x,bottom_y = var.keypoints.xy.squeeze(0)[0].cpu().numpy()
    top_x,top_y = var.keypoints.xy.squeeze(0)[1].cpu().numpy()

    # Calculate corner coordinates
    bbox = var.boxes.xywh.squeeze(0).cpu().numpy()
    x_center,y_center, width, height = bbox
    half_width = width / 2
    half_height = height / 2
    top_left = (x_center - half_width, y_center - half_height)
    top_right = (x_center + half_width, y_center - half_height)
    bottom_left = (x_center - half_width, y_center + half_height)
    bottom_right = (x_center + half_width, y_center + half_height)
    return bottom_x, bottom_y, top_x, top_y, bbox