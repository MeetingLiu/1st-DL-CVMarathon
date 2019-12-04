#!/usr/bin/env python
# coding: utf-8

# # 作業
# 
# 思考一下我們前面有提到圖片是矩陣，但維度可能會不一樣
# 例如灰階圖只有兩個維度，RGB 彩圖則有 3 個維度
# 
# 假如今天我們把 RGB 3 個維度拆開來看會有甚麼不同的效果呢？

# In[1]:


import numpy as np
import cv2

img_path = 'C:/Users/Meeting/DeepLearning/Part01/Part01/lena.png'

image = cv2.imread(img_path)
cv2.imshow('Original', image)
cv2.waitKey(0)

# R,G,B分量的提取
(B, G, R) = cv2.split(image) # 提取R,G,B分量
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

