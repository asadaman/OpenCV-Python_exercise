import cv2
import numpy as np

img = cv2.imread('star.jpg',0)
ret,thresh = cv2.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)

print(M)


# centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('centroid:(' + str(cx) + ',' + str(cy)+')')


# area
area = cv2.contourArea(cnt)
print('area:' + str(area))

# perimeter
perimeter = cv2.arcLength(cnt, True)
print('perimeter:' + str(perimeter))


