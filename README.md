# WechatGameAutoPlayer
Using Python Play the Wechat Games
###加减大师辅助设计
##实现原理：利用模板匹配

###难点： 1.截图的速度
         2.如何将目标区域自动裁剪成可以进行模板匹配的单个字符图片
         3.控制鼠标进行点击

###实现原理：1.调动系统函数进行截图操作（唯快不破！）
            2.自动横向切割&纵向切割 保存并resize成统一字符大小 如（30,60），标准模板字符同样归一化大小
            3.将待识别的字符集与标准模板字符进行一一比对，确定出字符的值，并组成表达式
                  note:(其中 “”=“” 可以不用比对 其默认在 cut_downer的第一个字符)
            4.进行简单的表达式真假值辨认，并控制鼠标进行相应的点击
### 操作步骤：
硬件： Pc + 安卓手机（安卓虚拟机也行？？）
0.******* ！！！注意 ！！！******
         第一步先删掉cut_temp 文件夹下的两张图片 那个是因为单个上传空文件夹无法上传我才填了两张照片，不删掉很有可能程序出错
1.安装相应的第三方库 大家都懂 差什么 pip什么 +电脑的投屏软件 （我用的ApowerMirror）
2.调整投屏软件的窗口 保证没有遮挡（这不是废话吗 逃。。）
3.用其他软件测出（QQ的截图之类的） 截取的目标区域在桌面上的位置并填入config文件中的相应参数里（有空逐一介绍对应的元素）
         截图效果如下：注意截取的目标区域中不能出现除了表达式其他的元素 比如右下角的小问号
         总么插入图片来着。。。。 
         算了有空再弄吧
         
4.运行 main.py 之后再等吧

###从来没玩过GitHub等我玩熟了再过了更新 补救一下####
         
