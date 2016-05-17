import cv2
import numpy as np

img = cv2.imread('star.jpg',0)
ret,thresh = cv2.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)


# Moments
cnt = contours[0]
M = cv2.moments(cnt)


# Aspect Ratio
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

print("aspect_ratio:" + str(aspect_ratio))


# Extent
area = cv2.contourArea(cnt)
x, y, w, h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

print("extent:" + str(extent))


# Solidity
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

print("solidity:" + str(solidity))


# Equivalent Diameter
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

print("equi_diameter:" + str(equi_diameter))


# Orientation
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print("orientation:" + str(angle))


# Mask and Pixel Points
mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)


# Maximum Value, Minimum Value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask = mask)

print("min_val:" + str(min_val))
print("max_val:" + str(max_val))
print("min_loc:" + str(min_loc))
print("max_loc:" + str(max_loc))


# Mean Color or Mean Intensity
mean_val = cv2.mean(img, mask = mask)

print("mean_val:" + str(mean_val))


# Extreme Points
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

print("leftmost:" + str(leftmost))
print("rightmost:" + str(rightmost))
print("topmost:" + str(topmost))
print("bottommost:" + str(bottommost))
