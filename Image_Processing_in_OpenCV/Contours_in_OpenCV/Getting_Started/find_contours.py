import numpy as np
import cv2

im = cv2.imread('box.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = 0

for contour in contours:
  print(contour)
  for p in contour:
    im = cv2.circle(im, (p[0][0], p[0][1]), 2, (255, 0, 0), -1)
    cnt += 1

print(cnt)
cv2.imwrite('result.png', im)
