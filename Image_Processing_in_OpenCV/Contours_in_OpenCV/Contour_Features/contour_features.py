import cv2
import numpy as np

img = cv2.imread('star.jpg',0)
ret,thresh = cv2.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)


# Moments
cnt = contours[0]
M = cv2.moments(cnt)

print('M:')
print(M)


# centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('centroid:(' + str(cx) + ',' + str(cy)+')')


# Contour Area
area = cv2.contourArea(cnt)

print('area:' + str(area))


# Contour Perimeter
perimeter = cv2.arcLength(cnt, True)

print('perimeter:' + str(perimeter))


# Contour Approximation
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

print('approx:' + str(approx))


# Convex Hull
hull = cv2.convexHull(cnt)

print('hull:' + str(hull))


# Checking Convexity
k = cv2.isContourConvex(cnt)

print('k:' + str(k))


# Straight Bounding Rectangle
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imwrite('straight_rectangle.png', img)


# Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

cv2.imwrite('rotated_rectangle.png', im)


# Minimum Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 2)


# Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im, ellipse, (0, 255, 0), 2)


# Fitting a Line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)
