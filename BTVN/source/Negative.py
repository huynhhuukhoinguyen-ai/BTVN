import cv2
import os

os.makedirs("output", exist_ok=True)
img_path = "anh1.png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

L = 256
img_neg = L - 1 - img

cv2.imshow('Original image', img)
cv2.imshow('Negative image', img_neg)
cv2.imwrite("output/1_negative.png", img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()