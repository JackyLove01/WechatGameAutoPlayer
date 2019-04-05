import os
import sys
import time
import traceback
import numpy as np
from pymouse import PyMouse
#from imgtools import *
from PIL import Image
from config import location_on_pc as loc,threshold
import cv2



def get_screenshot():
    if sys.platform == 'win32':
        from PIL import ImageGrab
        scr = ImageGrab.grab([loc['left_top_x'], loc['left_top_y'], loc['right_buttom_x'], loc['right_buttom_y']])
        return scr
    elif sys.platform == 'linux':
        cmd = 'import -window root -crop {0}x{1}+{2}+{3} screenshot.png'
        cmd = cmd.format(loc['right_buttom_x'] - loc['left_top_x'], loc['right_buttom_y'] - loc['left_top_y'],
                         loc['left_top_x'], loc['left_top_y'])
        os.system(cmd)
        scr = Image.open('screenshot.png')
        return scr
    else:
        print('Unsupported platform: ', sys.platform)
        sys.exit()

for i in range(20):
    filename = str(i) +".png"
    img = get_screenshot()  
    img.save(filename)
    time.sleep(1)
