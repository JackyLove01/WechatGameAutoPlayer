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
from img_process import binarize,S_cut,Z_cut
#from MatchTemplate_Test_Nomalization import Chars_recognition


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




        

def Chars_recognition(cut_char_filename):
    '''
    输入 单张待识别的字符图片 
    与标准模板字符进行一一匹配，得到字符对应的值
    '''
    list1 = [0,1,2,3,4,5,6,7,8,9,"-","+","="]
    d = {}
    

    for i in list1:
        filename = "Template/source/Themaplate/"+str(i)+".png"
        img = cv2.imread(cut_char_filename,1)
        gray = cv2.imread(cut_char_filename,0)


        img_template = cv2.imread(filename,0)

        #模板字符图片的宽 高
        w , h = img_template.shape[::-1]
        #print(w,h)

        #代识别字符的信息
        weight , height = gray.shape[::-1]

        ##2.将模板resize成待识别字符的大小

        img_template_resized = cv2.resize(img_template,(weight,height))
        #模板匹配的操作
        res = cv2.matchTemplate(gray,img_template_resized,cv2.TM_SQDIFF_NORMED)

        #得到最大和最小值的位置
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

        #print(min_val)
        #print(max_val)
        d[str(i)] = max_val

        #top_left = min_loc#左上角的位置
        #bottom_right = (top_left[0]+w,top_left[1]+h)#右下角的位置
    #print(d)
    list2 = list(d.items())
    #print(list2)
    list2.sort(key=lambda x:x[1])
    #print(list2)

    #print("{}字符识别结果为：{}".format(cut_char_filename[9:],list2[0][0]))
    return list2[0][0]
        #原图上做标注！
        #cv2.rectangle(img,top_left,bottom_right,(0,0,255),2)

        #cv2.imshow("win1_source",img_template)
        #cv2.imshow("win2_match",img)
        #cv2.waitKey(0)

def mouse_click(flag):
    if flag :
        m.click(loc["click_true_x"],loc['click_true_y'],1)
    else:
        m.click(loc["click_false_x"],loc['click_false_y'],1)

#def strings_process():
    '''
    return flag
    '''
 #   pass
 
def clear_temp():
    ls = os.listdir("cut_temp")
    #print(ls)
    for i in ls:
        os.remove("cut_temp/"+i)
def main():
    region = get_screenshot()
    #此时configure文件的上下边界 应该紧贴 目标字符的上下边界
    #左右边界则”无限“放宽
    #print(type(region))
    #Image._show(region)

    bin_img = binarize(region)

    S_cut(bin_img)#

    up_num,down_num = Z_cut()
    #up_num,down_num = 3,2
   # Chars_recognition(cut_char_filename)
    #及时清理掉cut_temp里的上次字符
    strings1 = ""
    strings2 = ""
    flag1 =0
    flag2 =0
    for maindir,subdir,temp_cut_char_name in os.walk("cut_temp"):
        #print(temp_cut_char_name)#temp_cut_name是列表形式
        #for i in temp_cut_char_name:
            #print(i)
            pass

    ### ERRORS ###
    for i in temp_cut_char_name:   
        if "cut_upper" == i[:9]and flag1 ==0:
            for num in range(up_num)  :
                strings1 += Chars_recognition("cut_temp/cut_upper"+str(num)+".png")
            flag1 = 1
            
    #for i in temp_cut_char_name:
        #print(i)
        if "cut_downer" == i[:10] and flag2==0:
            for num in range(down_num):
                strings2 += Chars_recognition("cut_temp/cut_downer"+str(num)+".png")
            flag2 = 1
            #Chars_recognition("Template/source/demo_match_recogitiom/tests/test04.png")
            
        

    ### ERRORS 解除 ###

    #print(strings1+strings2)
    history_Q = strings1+strings2
    print(history_Q)
    print(eval(strings1)==eval(strings2[1:]))
    output = (eval(strings1)==eval(strings2[1:]))
    mouse_click(output)
    #简易防止卡顿未刷新 从而重复点击上次的结果
    time.sleep(0.6)
    clear_temp()
        
    #cv2.imshow("windosw111",bin_img)
    #cv2.waitKey(0)
    #clear_temp()
if __name__ == "__main__":

    #jici = 0
    #t1 = time.time()
    m = PyMouse()
    
    while True:
        main()
        #jici+=1

    #t2 = time.time()

   # print(t2-t1)
    #print(jici)
    


    

    #[img_up ,img_down] = horizontal_cut(bin_img)
    #Image.SAVE("temp_source",region)
    
    #cv2.imwrite("temp_source.png",region)
