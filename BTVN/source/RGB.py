import cv2
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh3.png")
img_b = img[:, :, 0]
img_g = img[:, :, 1]
img_r = img[:, :, 2]
cv2.imshow('Original Image', img)
cv2.imshow('Red Channel', img_r)
cv2.imshow('Green Channel', img_g)
cv2.imshow('Blue Channel', img_b)
cv2.imwrite("output/11_rgb_original.png", img)
cv2.imwrite("output/11_rgb_r.png", img_r)
cv2.imwrite("output/11_rgb_g.png", img_g)
cv2.imwrite("output/11_rgb_b.png", img_b)
cv2.waitKey(0)
cv2.destroyAllWindows()