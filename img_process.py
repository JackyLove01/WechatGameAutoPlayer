#coding=utf-8

import os
import time
from PIL import Image
from pymouse import PyMouse
import cv2
import numpy as np 

#此模块的输入为 Windows截图 数据类型是？？

def binarize(img):
    '''
    functions:
    将截取的图片进行二值化
    '''
    #将PIL.Image.Image转化为OpenCV的格式 并转为灰度化图像
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2GRAY)

    #设定阈值 进行二值化
    threshold = 200
    param = cv2.THRESH_BINARY

    ret,processed = cv2.threshold(img,threshold,255,param)

    #print(type(processed))
    #cv2.imshow("win100",img)
    #cv2.imshow("win001",processed)
    #cv2.waitKey(0)
    return processed#返回类型为numpy.ndarray的二值化图像

def S_cut(img):#此处先进行手动切图的尝试 顺便加快速度 滑稽


#方法一：手动
# 手动横向切图 对切图的边界有要求 故先舍弃该方法
    #upper_img = [0,40] 1-40行
    #downer_img = [-40:] 倒数四十行到最后
    '''
    cv2.imwrite("cut_temp\cut_upper.png",img[:40])
    cv2.imwrite("cut_temp\cut_downer.png",img[img.shape[0]-40:])
    '''

#方法二： 自动 同Z_cut()

    ls1 = []
    ls2 = []

    flag_up = 1
    flag_down = 0
    for x in range(img.shape[0]):

        if img[x,...].any():
            ls1.append(1)

        else:
            ls1.append(0)

    flag_BJ = 1
    i = 0
    while True:
        if i >(len(ls1)-1):
            break
        if ls1[i] == 1 and flag_BJ:
            flag_BJ = 0
            x_up = i
            for j in range(i+1,len(ls1)):
                i = j
                if ls1[j] == 0 and not(flag_BJ):
                    x_down = j
                    flag_BJ = 1
                    ls2.append((x_up,x_down))            
                    break
        i+=1
        
    #print(ls2)   
    
    cv2.imwrite("cut2\cut_upper.png",img[ls2[0][0]:ls2[0][1]])
    cv2.imwrite("cut2\cut_downer.png",img[ls2[1][0]:ls2[1][1]])
    

    '''
    水平切割 固定切成上下两块 返回两张图片 类型为numpy.ndarray?也可能是保存为两张图片
    '''
    '''#自动横向水平分割法#
    #先弃用#
    num = 0
    list1 = []
    print(img.ndim)
    print(img.shape)
    for i in range(img.shape[0]):
        if img[i,...].any() != 0:
            if num == 0:
                list1.append(i)
        num+=1
            #print(i) 
        if num >= 1:
            if img[i,...].all() == 0:
                print(i)
                break
    '''          
    


def Z_cut():
    nums = 0
    list_img_name = ["cut2\cut_upper.png","cut2\cut_downer.png"]
### It seems that it has worked   ###
    for temp_name in list_img_name:

        img = cv2.imread(temp_name,0)#??
        #print(img.shape)
        ls1 = []
        ls2 = []

        flag_left = 1
        flag_right = 0
        for x in range(img.shape[1]):

            if img[...,x].any():
                ls1.append(1)

            else:
                ls1.append(0)

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
            
        #print(ls2)
        if temp_name ==   "cut2\cut_upper.png":
            cut_up_num = len(ls2)
        elif temp_name == "cut2\cut_downer.png":
            cut_down_num = len(ls2)
        #批次问题 即 是upper的还是downer的
        for i in range(len(ls2)):
            
            cv2.imwrite( "cut_temp"+temp_name[4:-4] +str(i)+".png",img[:,ls2[i][0]:ls2[i][1]])
    
    return (cut_up_num,cut_down_num)

    """纵向切割"""
    """print(img.size)
    _, height = img.size
    px = list(np.sum(np.array(img) == 0, axis=0))
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(px)):
        if px[x] > 1:
            x0.append(x)

    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            cut_list.extend([x0[i - 1], x0[i]])
    cut_list.append(x0[-1])

    cut_imgs = []
    # 切割顺利的话应该是整对
    if len(cut_list) % 2 == 0:
        #print(len(cut_list))
        for i in range(len(cut_list) // 2):
            cut_img = img.crop([cut_list[i * 2], 0, cut_list[i * 2 + 1], height])
            
            cut_imgs.append(cut_img)
            cut_img = np.array(cut_img)
            #print("1")
            cv2.imwrite("cut_temp/upper_"+str(i)+".png",cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')

"""

# def Z_cut():#函数将两张图片 切割成单字符并按次序把存在 cut_temp 里
#     '''
#     输入单张 单行数字，运算符的图片
#     返回 若干张切割好的有次序大小一致的单字符图片
#     '''

    
#     flag1 = 0
#     flag2 =0
#     x1_list = []
#     x2_list = []
#     #上半部分 cut_upper
#     cut_upper = cv2.imread("cut_temp\cut_upper.png",0)
#     # cv2.imshow("dads",cut_upper)
#     # cv2.waitKey(0)
#     #print(cut_upper.shape[1])
#     #print(cut_upper[...,32])
#     #print(cut_upper[...,130].all() == 0 and flag1 == 1)
    
#     start_index = -1
#     end = -1
#     index = 0
#     for x in range(cut_upper.shape[1]):
#         #if cut_upper[...,x].all() == 0 and flag1 == 0:
#         #    pass
        
#         if (cut_upper[...,x].any() != 0):
            
#             #print(x)
#             x1_list.append(x)
            
            
#         # if (cut_upper[...,x].all() == 0) and (flag1 == 1):
#         #     flag1 = 0
#         #     #print(x)
#         #     x2_list.append(x)
            
            
#         #if  cut_upper[...,x].any() != 0 and flag1 ==1:
#         #    pass
#     print(x1_list)
#     print(x2_list)

        
#     #下半部分 cut_downer
#     cut_downer = cv2.imread("cut_temp\cut_downer.png",0)
    

    
#     #版本1 继续用递归？？？
#     #切割单字符次序编号
#     """i = 0
#     x1_list = []
#     x2_list = []
#     cut_upper = cv2.imread("cut_temp\cut_upper.png",0)#
#     cut_downer = cv2.imread("cut_temp\cut_downer.png",0)#0表示通道数？？
#     #print(cut_downer.shape) #(40,178)= height,weight
#     for i in range(cut_upper.shape[1]):
#         if cut_upper[...,i].any() != 0:
#             print(cut_upper[...,i])
#             print(len(cut_upper[...,i]))#40 截取的上区域的高度 40 okay
#             x1_list.append(i)
            
#             for j in range(i,cut_upper.shape[1]):
#                 if cut_upper[...,j].any() == 0:
#                     x1_list.append(j)
#                     break
            
#             break

    
#     print(x1_list)
#     cv2.imwrite("cut_temp\cut_downer_test.png",cut_upper[...,i:j])"""
    

def main():
    #img = Image.open("001.png")
    
    img = Image.open("0.png")#windows 截图的上下边界 应该紧贴 目标字符的上下边界
    #img = cv2.imread("xincuttest.png",0)
    img_uncut = binarize(img)
    S_cut(img_uncut)
    up_num,down_num = Z_cut()
    print(up_num,down_num)
    
    #Z_cut()
    #Image._show(vertical_cut(img))
    #print(vertical_cut(img))
    #cv2.imshow("windosws",Z_cut(cv2.imread("cut_upper.png",0)))
    #cv2.waitKey(0)

if __name__ == "__main__":

    t1 = time.time()
    main()
    t2 = time.time()
    print(t2-t1)