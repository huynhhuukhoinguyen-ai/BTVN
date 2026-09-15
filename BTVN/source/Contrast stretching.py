import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img_path = "anh2.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
low_contrast_img = np.uint8(img * (70.0 / 255.0) + 90)
rmin = float(np.min(low_contrast_img))
rmax = float(np.max(low_contrast_img))
def ContrastStretching(img, r1, r2, s1, s2):
    W, H = img.shape
    img_contrast = np.zeros((W, H), np.uint8)
    for x in range(0, W):
        for y in range(0, H):
            r = img[x, y]
            if (r <= r1):
                s = (s1 / r1) * r if r1 != 0 else 0
            elif ((r > r1) & (r <= r2)):
                s = (s2 - s1) / (r2 - r1) * r + (s1 * r2 - s2 * r1) / (r2 - r1)
            else:
                s = (255 - s2) / (255 - r2) * r + (255 * (s2 - r2)) / (255 - r2)
            img_contrast[x, y] = np.uint8(s)
    return img_contrast

img_stretched = ContrastStretching(low_contrast_img, rmin, rmax, 0.0, 255.0)

cv2.imshow('Contrast Stretched Output', low_contrast_img)
cv2.imshow('Original Image', img_stretched)
cv2.imwrite("output/4_low_contrast_input.png", low_contrast_img)
cv2.imwrite("output/4_contrast_stretching.png", img_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()