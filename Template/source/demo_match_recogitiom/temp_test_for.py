import cv2
import numpy as np 



#resize 归一化
#1.双方都resize成同一个
#2.模板resize成待识别字符的大小
#3.切割好的字符大小经过比对 分类 进行二次判断


img = cv2.imread("cut_downer_test.png",1)
gray = cv2.imread("cut_downer_test.png",0)


img_template = cv2.imread("+.png",0)

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
print(max_val)
top_left = min_loc#左上角的位置
bottom_right = (top_left[0]+w,top_left[1]+h)#右下角的位置

#原图上做标注！
cv2.rectangle(img,top_left,bottom_right,(0,0,255),2)

#cv2.imshow("win1_source",img_template)
#cv2.imshow("win2_match",img)
#cv2.waitKey(0)

