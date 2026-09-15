import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh2.png", cv2.IMREAD_GRAYSCALE)
mask = np.array([[0, 1, 0],
                 [1, -4, 1],
                 [0, 1, 0]], dtype=np.int32)
def Laplacian(img, mask):
    a = 1
    img_pad = np.pad(img, a, mode="constant", constant_values=0)
    H, W = img.shape
    img_laplacian = np.zeros((H, W), dtype=np.int32)
    for x in range(H):
        for y in range(W):
            total = 0
            for s in range(-a, a + 1):
                for t in range(-a, a + 1):
                    total += img_pad[x + a + s, y + a + t] * mask[s + a, t + a]
            img_laplacian[x, y] = total
    return img_laplacian
lap = Laplacian(img, mask)
lap_scaled = 255 * (lap - np.min(lap)) / (np.max(lap) - np.min(lap))
lap_scaled = np.uint8(lap_scaled)
img_sharp = np.clip(img.astype(np.int32) - lap, 0, 255).astype(np.uint8)
cv2.imshow('Original image', img)
cv2.imshow('Laplacian Edge', lap_scaled)
cv2.imshow('Sharpened image', img_sharp)
cv2.imwrite("output/8_laplacian_edge.png", lap_scaled)
cv2.imwrite("output/8_laplacian_sharp.png", img_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()