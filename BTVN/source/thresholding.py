import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)
img_path = "anh1.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

W, H = img.shape
img_threshold = np.zeros((W, H), np.uint8)

for x in range(0, W):
    for y in range(0, H):
        r = img[x, y]
        if r > 50:
            img_threshold[x, y] = 255
        else:
            img_threshold[x, y] = 0

cv2.imshow('Original image', img)
cv2.imshow('Thresholding image', img_threshold)
cv2.imwrite("output/5_thresholding.png", img_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()