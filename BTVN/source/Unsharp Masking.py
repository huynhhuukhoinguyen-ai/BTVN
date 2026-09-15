import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh2.png", cv2.IMREAD_GRAYSCALE)
img_f = img.astype(np.float32)
k = 5
kernel = np.ones((k, k), np.float32) / (k * k)
img_blur = cv2.filter2D(img_f, -1, kernel)
mask = img_f - img_blur
k_sharp = 1.0
sharp = np.clip(img_f + k_sharp * mask, 0, 255).astype(np.uint8)
mask_display = cv2.normalize(mask, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imshow('Original image', img)
cv2.imshow('Unsharp Mask', mask_display)
cv2.imshow('Sharpened image', sharp)
cv2.imwrite("output/9_unsharp_mask.png", mask_display)
cv2.imwrite("output/9_unsharp_result.png", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()