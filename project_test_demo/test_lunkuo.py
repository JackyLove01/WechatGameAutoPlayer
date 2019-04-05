import cv2


img = cv2.imread("Template\source\bin\0.png",0)

image,contours,hierarchy = cv2.findContours(img,2,2)#此处等号会出问题 识别出两个 -- 或==

#bug2 水平切割 边界 没有预留 即上下边界没有留白则很有可能框选不出来
flag =1
i=0
ls = []
for cnt in contours:

    x,y,w,h = cv2.boundingRect(cnt)


    if x!=0 and y!=0 and w*h>80:
        print(x,y,w,h)
        ls.append([x,y,w,h])
        i+=1


ls.sort(key = lambda x:x[0])

print(ls)

for i in  range(len(ls)):
    
    cv2.imwrite("cut_temp/up"+str(i)+".png",img[0:40,ls[i][0]:ls[i][0]+ls[i][2]])
        
