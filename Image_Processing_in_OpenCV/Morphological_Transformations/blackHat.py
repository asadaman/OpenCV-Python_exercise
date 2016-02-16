import cv2
import numpy as np

img = cv2.imread('j.png', 0)
kernel = np.ones((9,9), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite('blackHat.png', result)
