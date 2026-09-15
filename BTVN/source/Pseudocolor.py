import cv2
import os
os.makedirs("output", exist_ok=True)
img = cv2.imread("anh3.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_pseudo = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', img_gray)
cv2.imshow('Pseudocolor Image', img_pseudo)
cv2.imwrite("output/14_pseudo_original.png", img)
cv2.imwrite("output/14_pseudo_gray.png", img_gray)
cv2.imwrite("output/14_pseudo_result.png", img_pseudo)
cv2.waitKey(0)
cv2.destroyAllWindows()