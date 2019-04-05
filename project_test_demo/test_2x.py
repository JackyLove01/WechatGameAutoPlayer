import cv2
import numpy as np 
from PIL import Image
import time
def S_cut(img):

    flag1 = 0
    flag2 = 0

    x1_list = []
    x2_list = []
    print(img.shape)#(height_Y,weith_X)
    #print(img[...,31])
    print(img[...,33].all())# == False
    print(img[...,34].any())# == True
    #print(img[...,33].all()==0)
    #print(img[...,34].any()!=0)
    #print(img[...,33].all()==0 and img[...,34].any()!=0)
    '''
    for i in range(img.shape[1]-1):
        if not(img[...,i].all()) and img[...,i+1].any() and flag1 == 0:
            x1_list.append(i)
            flag1 = 1
        
        if img[...,i].any() and not(img[...,i+1].all()) and flag1 ==1:
            x2_list.append(i+1)
            flag1 = 0
            
    print(x1_list,x2_list)
    '''



    for x in range(1,img.shape[1]-1):
        if  not(img[...,x-1].all()and img[...,x].any())and img[...,x+1].any()  and flag1 == 0 :
            x1_list.append(x)
            flag1 = 1
           

        if img[...,x].any() and not(img[...,x+1].all()) and (img[...,x-1].any()) and flag1 == 1:

            x2_list.append(x+1)
            flag1 = 0
            
    print(x1_list,x2_list)



def Z_cut(img):
    print(img.shape)
    ls1 = []
    ls2 = []

    flag_left = 1
    flag_right = 0
    for x in range(img.shape[1]):

        if img[...,x].any():
            ls1.append(1)

        else:
            ls1.append(0)
    #print(ls1)


### It seems that it has worked   ###
    flag_BJ = 1
    i = 0
    while True:
        if i >(len(ls1)-1):
            break
        if ls1[i] == 1 and flag_BJ:
            flag_BJ = 0
            x_left = i
            for j in range(i+1,len(ls1)):
                i = j
                if ls1[j] == 0 and not(flag_BJ):
                    x_right = j
                    flag_BJ = 1
                    ls2.append((x_left,x_right))            
                    break
        i+=1
        
    print(ls2)   
    #     if img[...,x].any() and flag_left==1:
    #         flag_left = 0
    #         flag_right = 1
    #         ls1.append(x)
    #     else :
    #         if flag_right == 1 and not(img[...,x].all()):
    #             flag_left = 1
    #             flag_right = 0
    #             ls2.append(x)

    # print(ls1,"\n",ls2)
    # """传入二值化后的图片进行垂直投影"""
    # pixdata = img.load()
    # w,h = img.size
    # print(w,h)
    # ver_list = []
    # # 开始投影
    # for x in range(w):
    #     black = 0
    #     for y in range(h):
    #         if pixdata[x,y] == 0:
    #             black += 1
    #     ver_list.append(black)
    # # 判断边界
    # l,r = 0,0
    # flag = False
    # cuts = []
    # for i,count in enumerate(ver_list):
    #     # 阈值这里为0
    #     if flag is False and count > 0:
    #         l = i
    #         flag = True
    #     if flag and count == 0:
    #         r = i-1
    #         flag = False
    #         cuts.append((l,r))
    # return cuts

t1 = time.time()

img = cv2.imread("cut_downer.png",0)

#img = Image.open("cut_upper.png")
Z_cut(img)
t2 = time.time()
print(t2-t1)
#img = cv2.imread("cut_upper.png",0)
# cv2.imshow("win",img)
# cv2.waitKey(0)
#S_cut(img)
#Z_cut()