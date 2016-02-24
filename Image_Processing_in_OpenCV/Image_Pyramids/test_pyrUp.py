import cv2
img = cv2.imread('lower_rezo3.jpg')
lower_rezo = img

for i in range(3):
  higher_rezo = cv2.pyrUp(lower_rezo)
  lower_rezo = higher_rezo

cv2.imwrite('higher_rezo.jpg', higher_rezo)


