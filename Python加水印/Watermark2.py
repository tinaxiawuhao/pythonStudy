# !usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np


def zh_ch(string):
    return string.encode('gbk').decode(errors='ignore')


# 为了操作方便我就只加灰度图了
# R，G，B原理一样每个通道加一下
# 要加水印照片
img = cv2.imread("results/FFT/kewayi.jpeg")
# 切割大小
dstImg = img[0:400,0:400]
# 隐藏水印照
mark = cv2.imread("results/FFT/mark.png")
# 展示水印照
cv2.imshow(zh_ch("mark"), mark)
# 将大于0转为 True
t_mark = mark[::] > 0
# 标记为1
mark[t_mark] = 1
# 提取原始图像大小
size = dstImg.shape
# 生成提取矩阵
t254 = np.ones(size, dtype=np.uint8) * 254
# 获取原始图像高7位
a7 = cv2.bitwise_and(dstImg, t254)
# 将水印放入最低位
e = cv2.bitwise_or(a7, mark)

cv2.imshow(zh_ch("原始图像"), dstImg)
cv2.imshow(zh_ch("加水印图像"), e)

##########################
# 提取水印过程

t1 = np.ones(size, dtype=np.uint8) * 1
wm = cv2.bitwise_and(e, t1)
w = wm[:, :] > 0
wm[w] = 255

cv2.imshow(zh_ch("提取水印"), wm)

cv2.waitKey()
cv2.destroyWindow()