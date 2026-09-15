import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh2.png", cv2.IMREAD_GRAYSCALE)
H, W = img.shape
img_f = img.astype(np.float32)
img_roberts = np.zeros((H, W), dtype=np.float32)
for x in range(H - 1):
    for y in range(W - 1):
        gx = img_f[x + 1, y + 1] - img_f[x, y]
        gy = img_f[x + 1, y] - img_f[x, y + 1]
        img_roberts[x, y] = np.abs(gx) + np.abs(gy)
img_roberts = np.clip(img_roberts, 0, 255).astype(np.uint8)
img_pad = np.pad(img_f, 1, mode='constant', constant_values=0)
img_sobel = np.zeros((H, W), dtype=np.float32)
for x in range(H):
    for y in range(W):
        w = img_pad[x:x+3, y:y+3]
        gx = (w[2, 0] + 2 * w[2, 1] + w[2, 2]) - (w[0, 0] + 2 * w[0, 1] + w[0, 2])
        gy = (w[0, 2] + 2 * w[1, 2] + w[2, 2]) - (w[0, 0] + 2 * w[1, 0] + w[2, 0])
        img_sobel[x, y] = np.abs(gx) + np.abs(gy)
img_sobel = np.clip(img_sobel, 0, 255).astype(np.uint8)
cv2.imshow('Original image', img)
cv2.imshow('Roberts Edge', img_roberts)
cv2.imshow('Sobel Edge', img_sobel)
cv2.imwrite("output/10_original.png", img)
cv2.imwrite("output/10_roberts.png", img_roberts)
cv2.imwrite("output/10_sobel.png", img_sobel)
cv2.waitKey(0)