# -*- coding: utf-8 -*-

import cv2

def movie_to_image(num_cut):
    output_path = './out/'  # 出力するフォルダパス

    capture = cv2.VideoCapture(0)
    img_count   = 0  # 保存した候補画像数
    frame_count = 0  # 読み込んだフレーム画像数

    # フレーム画像がある限りループ
    while(capture.isOpened()):
      # フレーム画像一枚取得
      ret, frame = capture.read()
      if ret == False:
          break

      # Display the resulting frame
      cv2.imshow('Video', frame)
      # 指定した数だけフレーム画像を間引いて保存
      # if frame_count % num_cut == 0:
      key = cv2.waitKey(10) & 0xFF
      if  key == ord('c'):
          img_file_name = output_path + str(img_count) + ".jpg"
          frame_resize = cv2.resize(frame, (640, 360))
          cv2.imwrite(img_file_name, frame_resize)
          img_count += 1

      frame_count += 1

      # if cv.waitKey(10) == 27:
      if key == ord('q'):
          break

    # キャプチャ構造体開放
    capture.release()

if __name__ == '__main__':    

    # 間引き数を10にしてフレーム画像抽出
    movie_to_image(int(10))
