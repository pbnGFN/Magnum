import mss
import mss.tools
import mss.screenshot
import mss.windows
import cv2
import numpy as np
import time


class WindowCapture:
    #properties
    monitor_number = 1
    with mss.mss() as sct:
            mon = sct.monitors[monitor_number]
    
    def __init__(self):
        
        self.monitor = {
        "top": self.mon["top"] ,
        "left": self.mon["left"] ,  
        "width": self.mon['width'],
        "height": self.mon['height'],
        "mon": self.monitor_number,
    }
        
    def get_screenshot(self)->str:
        output = r"images\wincap.png"

        # Grab the data
        with mss.mss() as sct:
            sct_img = sct.grab(self.monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return output