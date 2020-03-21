# -*- coding: utf-8 -*-

import cv2
import os
import glob

ImgSize = (32,32)

SearchName = ["face","other"]

# SearchName 
for i in range(len(SearchName)):
  name = SearchName[i]
  # img_file_name_list=os.listdir("./outputs/"+name)
  # print("Number of {}: {}".format(name, len(img_file_name_list)))
  in_dir = "./outputs/"+name+"/*"
  in_jpg=glob.glob(in_dir)

  out_dir = "./train_data/"+name
  os.makedirs(out_dir, exist_ok=True)

  for i in range(len(in_jpg)):
    file_name = in_jpg[i]
    print(file_name)
    #print(str(in_jpg[i]))
    img    = cv2.imread(str(in_jpg[i]))
    img_re = cv2.resize(img,ImgSize)
    fileName=os.path.join(out_dir,str(i)+".jpg")
    cv2.imwrite(str(fileName),img_re)


# img_file_name = output_path + str(img_count) + ".jpg"
# frame_resize = cv2.resize(frame, img_size)
# cv2.imwrite(img_file_name, frame_resize)
# img_count += 1
