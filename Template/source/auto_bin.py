import cv2
import numpy as np 
from PIL import Image


def binarize(img):
    '''
    functions:
    将截取的图片进行二值化
    '''
    #--将PIL.Image.Image转化为OpenCV的格式 
    # 并转为灰度化图像
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #设定阈值 进行二值化
    threshold = 200
    param = cv2.THRESH_BINARY

    ret,processed = cv2.threshold(img,threshold,255,param)

    print(type(processed))
    #cv2.imshow("win100",img)
    #cv2.imshow("win001",processed)
    #cv2.waitKey(0)
    return processed#返回类型为numpy.ndarray的二值化图像


for i in range(0,13):
    filename = str(i)+".png"
    print(filename)
    temp = cv2.imread(filename)
    #cv2.imshow(filename,temp)
    #cv2.waitKey(0)
    cv2.imwrite("bin/"+filename,binarize(temp))
