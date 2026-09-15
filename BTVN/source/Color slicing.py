import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("data/anh3.png")
H, W, _ = img.shape
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
black_bg = np.zeros_like(img)
img_sliced = np.where(mask[:, :, None] == 255, img, black_bg)
cv2.imshow('Original Image', img)
cv2.imshow('Color Slicing Mask', mask)
cv2.imshow('Color Slicing Result', img_sliced)
cv2.imwrite("output/15_color_slicing_mask.png", mask)
cv2.imwrite("output/15_color_slicing_result.png", img_sliced)
cv2.waitKey(0)
cv2.destroyAllWindows()
