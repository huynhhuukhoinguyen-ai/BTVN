import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
img_path = "anh2.png"
img_original = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
noise_img = img_original.copy()
num_noise = int(0.03 * img_original.size)
coords_white = [np.random.randint(0, i, num_noise) for i in img_original.shape]
noise_img[tuple(coords_white)] = 255
coords_black = [np.random.randint(0, i, num_noise) for i in img_original.shape]
noise_img[tuple(coords_black)] = 0

def MedianFilter(img, size):
    a = size // 2
    img_pad = np.pad(img, a, mode="constant", constant_values=0)
    H, W = img.shape
    img_out = np.zeros((H, W), np.uint8)
    for x in range(H):
        for y in range(W):
            w = np.zeros((size, size), np.uint8)
            for s in range(-a, a + 1):
                for t in range(-a, a + 1):
                    w[a + s, a + t] = img_pad[x + a + s, y + a + t]
            w_1D = np.reshape(w, (size * size,))
            w_sort = np.sort(w_1D)
            median = w_sort[(size * size) // 2]
            img_out[x, y] = median
    return img_out
img_median = MedianFilter(noise_img, 3)
cv2.imshow('Original image', img_original)
cv2.imshow('Salt-and-Pepper Noisy input', noise_img)
cv2.imshow('Median Filter Output', img_median)
cv2.imwrite("output/7_median_original.png", img_original)
cv2.imwrite("output/7_median_noisy.png", noise_img)
cv2.imwrite("output/7_median_output.png", img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()