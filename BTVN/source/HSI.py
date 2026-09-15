import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh3.png")
H, W, _ = img.shape
img_norm = img.astype(np.float32) / 255.0
B = img_norm[:, :, 0]
G = img_norm[:, :, 1]
R = img_norm[:, :, 2]
img_H = np.zeros((H, W), dtype=np.float32)
img_S = np.zeros((H, W), dtype=np.float32)
img_I = np.zeros((H, W), dtype=np.float32)
for y in range(H):
    for x in range(W):
        r, g, b = R[y, x], G[y, x], B[y, x]
        i = (r + g + b) / 3.0
        img_I[y, x] = i
        if (r + g + b) > 0:
            s = 1.0 - (3.0 / (r + g + b)) * min(r, g, b)
        else:
            s = 0.0
        img_S[y, x] = s
        num = 0.5 * ((r - g) + (r - b))
        den = np.sqrt((r - g)**2 + (r - b)*(g - b)) + 1e-6
        theta = np.arccos(np.clip(num / den, -1.0, 1.0)) * (180.0 / np.pi)
        if b <= g:
            img_H[y, x] = theta
        else:
            img_H[y, x] = 360.0 - theta
h_disp = np.uint8((img_H / 360.0) * 255)
s_disp = np.uint8(img_S * 255)
i_disp = np.uint8(img_I * 255)
cv2.imshow('Original Image', img)
cv2.imshow('Hue Channel', h_disp)
cv2.imshow('Saturation Channel', s_disp)
cv2.imshow('Intensity Channel', i_disp)
cv2.imwrite("output/13_hsi_hue.png", h_disp)
cv2.imwrite("output/13_hsi_saturation.png", s_disp)
cv2.imwrite("output/13_hsi_intensity.png", i_disp)
cv2.waitKey(0)
cv2.destroyAllWindows()