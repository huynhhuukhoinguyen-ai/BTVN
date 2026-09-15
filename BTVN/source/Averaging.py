import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh2.png", cv2.IMREAD_GRAYSCALE)
k = 5
a = k // 2
img_pad = np.pad(img, a, mode='constant', constant_values=0)
H, W = img.shape
img_out = np.zeros((H, W), np.uint8)

for y in range(H):
    for x in range(W):
        total = 0
        for s in range(-a, a + 1):
            for t in range(-a, a + 1):
                total += int(img_pad[y + a + s, x + a + t])
        img_out[y, x] = total // (k * k)
cv2.imshow('Original image', img)
cv2.imshow('Averaging filter image (k=5)', img_out)
cv2.imwrite("output/6_averaging_input.png", img)
cv2.imwrite("output/6_averaging_output.png", img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()