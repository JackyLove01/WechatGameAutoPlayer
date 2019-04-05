from PIL import Image
import os
import sys
import time
import traceback
import numpy as np
from pymouse import PyMouse
import cv2
from config import location_on_pc as loc,threshold








def get_screenshot():
    '''
    Welcom to descriptions about get_screenshot
    '''
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


def binarize(img, threshold=threshold):
    """二值化"""
    img = img.convert('L')
    table = []
    for i in range(256):
        if i > threshold:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')
    return bin_img
c = 0
def v_cut(img):
    global c
    """竖直方向切割图片"""
    print(type(img))
    sum_list = np.array(img).sum(axis=1)
    print(type(sum_list))
    start_index = -1
    end = -1
    index = 0
    for sum in sum_list:
        if sum.any() > 255 * 2:#JACKYLOVE修改  if sum > 255 * 2:
            start_index = index
            break
        index += 1
    for i in range(1, len(sum_list) + 1):
        if sum_list[-i].any() > 255 * 2:#JACKYLOVE修改if sum_list[-i] > 255 * 2:
            end = len(sum_list) + 1 - i
            break
    img = img[start_index:end, :]
    img = cv2.resize(img, (30, 60), interpolation=cv2.INTER_CUBIC)
    #cv2.imwrite('SingleChar/%d.png' %c, img)
    c += 1
    return img





print(help(get_screenshot))
#img = get_screenshot()
img = cv2.imread("001.png",0)


imgs = v_cut(img)

cv2.imshow("win2",imgs)