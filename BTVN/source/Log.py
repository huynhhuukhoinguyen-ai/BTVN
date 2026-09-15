import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)
img_path = "anh1.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

c = 255 / np.log(255 + 1)
img_log = np.uint8(c * np.log(1.0 + img))

cv2.imshow('Original image', img)
cv2.imshow('Log Transfromation image', img_log)
cv2.imwrite("output/2_log.png", img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()