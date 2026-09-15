import cv2
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh3.png")
img_b = img[:, :, 0]
img_g = img[:, :, 1]
img_r = img[:, :, 2]
img_cyan = 255 - img_r
img_magenta = 255 - img_g
img_yellow = 255 - img_b
cv2.imshow('Original Image', img)
cv2.imshow('Cyan Channel', img_cyan)
cv2.imshow('Magenta Channel', img_magenta)
cv2.imshow('Yellow Channel', img_yellow)
cv2.imwrite("output/12_cmy_cyan.png", img_cyan)
cv2.imwrite("output/12_cmy_magenta.png", img_magenta)
cv2.imwrite("output/12_cmy_yellow.png", img_yellow)
cv2.waitKey(0)
cv2.destroyAllWindows()