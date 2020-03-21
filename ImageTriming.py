# -*- coding: utf-8 -*-

import cv2
import os
import glob

ImgSize = (32,32)

img_file = "./out/0.jpg"

img    = cv2.imread(str(img_file))
height = img.shape[0]
width  = img.shape[1]
for i in range(int(width/32)):
  for j in range(3): # range(int(width/32)):
    img_file_name = "./outputs/other/"+str(i)+".jpg"
    top  = 32 * j
    left = 32 * i
    # dst = img.astype(np.uint8)[top:top+32, left:left+32]
    dst = img[top:top+32, left:left+32]
    cv2.imwrite(img_file_name, dst)
