# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:04:44 2018

@author: Administrator
用于测试从图像中获取指定矩形区域的中心点坐标
"""
import numpy as np
import cv2
import sys
import os
def main_process(sourceImg):
    img = cv2.imread(sourceImg)
    title = 'cv2py'
    cv2.namedWindow(title)
    print("1111")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("source img", img)
    #img = gray
# =============================================================================
#    高斯滤波
# =============================================================================
    imblur = cv2.GaussianBlur(gray, (3,3), 1.5)
    #cv2.imshow(title,imblur)
    cv2.waitKey(1000)
# =============================================================================
#     阈值化处理
# =============================================================================
    retval,bina = cv2.threshold(imblur, 200, 255,0)
    #cv2.imshow(title, bina)
   
    #thresh = cv2.adaptiveThreshold(imblur, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    #cv2.imshow(title, thresh)
    cv2.waitKey(150)
   
# =============================================================================
#     边缘检测
# =============================================================================
    canny = cv2.Canny(bina, 50, 130, 3)
    cv2.imshow("after canny", canny)
    cv2.waitKey(1500)
# =============================================================================
#    轮廓提取
# =============================================================================
    _,cts, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   
    contour_count = len(cts)
    print("contour count is %d"%contour_count)
    
    for i in range(0, len(cts)):
        rect = cv2.minAreaRect(cts[i]) #获取最小外接矩形,cts[i]代表一个连通区域
        x, y = rect[0]
        if (1000<  cv2.contourArea(cts[i])):
            cv2.circle(img, (int(x), int(y)), 3, (0, 255, 255), 5)  #绘制区域的中心点
            cv2.drawContours(img, cts[i], -1, (255, 255, 0), 3) #绘制区域的轮廓
            print("x=%s, y=%s,size=%d"%(x,y, cv2.contourArea(cts[i])))

    cv2.imshow("after drawContour", canny);
    cv2.imshow("source img", img)
    cv2.waitKey(25500)
    cv2.destroyAllWindows()
    
    return;
    
    
    
if __name__ == "__main__":
    print("hello world")
    main_process("timg.jpg")

