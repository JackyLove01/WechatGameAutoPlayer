import cv2
import numpy as np 

img = cv2.imread("001.png",1)
gray = cv2.imread("001.png",0)


img_template = cv2.imread("T1.png",0)

#模板字符图片的宽 高
w , h = img_template.shape[::-1]
print(w,h)





#模板匹配的操作
res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF_NORMED)

#得到最大和最小值的位置
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

top_left = min_loc#左上角的位置
bottom_right = (top_left[0]+w,top_left[1]+h)#右下角的位置

#原图上做标注！
cv2.rectangle(img,top_left,bottom_right,(0,0,255),2)

cv2.imshow("win1_source",img_template)
cv2.imshow("win2_match",img)
cv2.waitKey(0)

