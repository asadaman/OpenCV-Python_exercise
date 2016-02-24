import cv2
img = cv2.imread('messi.jpg')

higher_rezo = img
for i in range(3):
  lower_rezo = cv2.pyrDown(higher_rezo)
  filename = 'lower_rezo' + str(i+1) + '.jpg'
  cv2.imwrite(filename, lower_rezo)
  higher_rezo = lower_rezo


