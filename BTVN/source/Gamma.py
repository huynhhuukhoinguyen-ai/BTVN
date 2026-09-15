import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)
img_path = "anh1.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

def GrammaTransform(img, gramma):
    W, H = img.shape
    img_gramma = np.zeros((W, H), np.uint8)
    c = np.power(255, 1 - gramma)
    for x in range(0, W):
        for y in range(0, H):
            r = img[x, y]
            s = c * np.power(r, gramma)
            img_gramma[x, y] = np.uint8(s)
    return img_gramma

img_gamma = GrammaTransform(img, 0.5)

cv2.imshow('Original image', img)
cv2.imshow('Gamma Transformation (gamma = 0.5)', img_gamma)
cv2.imwrite("output/3_gamma_0.5.png", img_gamma)

cv2.waitKey(0)
cv2.destroyAllWindows()