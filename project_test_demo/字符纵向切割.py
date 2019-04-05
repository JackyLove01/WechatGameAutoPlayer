#coding:utf8
import os
from PIL import Image,ImageDraw,ImageFile
import numpy
import pytesseract
import cv2
import imagehash
import collections
class pictureIdenti:

    #rownum：切割行数；colnum：切割列数；dstpath：图片文件路径；img_name：要切割的图片文件
    def splitimage(self, rownum=1, colnum=4, dstpath="",
                   img_name="cut_upper.png",):
        img = Image.open(img_name)
        w, h = img.size
        if rownum <= h and colnum <= w:
            print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
            print('开始处理图片切割, 请稍候...')

            s = os.path.split(img_name)
            if dstpath == '':
                dstpath = s[0]
            fn = s[1].split('.')
            basename = fn[0]
            ext = fn[-1]

            num = 1
            rowheight = h // rownum
            colwidth = w // colnum
            file_list = []
            for r in range(rownum):
                index = 0
                for c in range(colnum):
                    # (left, upper, right, lower)
                    # box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                    if index<1:
                        colwid = colwidth+6
                    elif index<2:
                        colwid = colwidth + 1
                    elif index < 3:
                        colwid = colwidth

                    box = (c * colwid, r * rowheight, (c + 1) * colwid, (r + 1) * rowheight)
                    newfile = os.path.join(dstpath, basename + '_' + str(num) + '.' + ext)
                    file_list.append(newfile)
                    img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                    num = num + 1
                    index+=1
            for f in file_list:
                print(f)
            print('图片切割完毕，共生成 %s 张小图片。' % num)


p1 =  pictureIdenti()
p1.splitimage( rownum=1, colnum=4, dstpath="",img_name="cut_upper.png",)
