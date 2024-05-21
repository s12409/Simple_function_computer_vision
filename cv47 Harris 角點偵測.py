'''cv47 海利斯(Harris)角點偵測'''
import cv2
import numpy as np

filename = 'data/building.jpg'
src = cv2.imread(filename) #讀取影像
src = cv2.resize(src, (0,0), fx=0.5, fy=0.5) #影像縮小一倍
img = src.copy() #複製影像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #轉換成灰階影像

gray = np.float32(gray) #將灰階影像轉換成浮點數格式
dst = cv2.cornerHarris(gray, 2, 3, 0.04) #海利斯角點偵測

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None) #角點膨脹

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255] #只顯示較明顯的角點
cv2.imshow('src', src)
cv2.imshow('dst', img), cv2.moveWindow('dst', 620,50)
if cv2.waitKey(0) & 0xff == 27: #按ESC離開
    cv2.destroyAllWindows()
