import cv2
import numpy as np,sys

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

G = A.copy()
gpA = [G]
for i in xrange(6):
  G = cv2.pyrDown(gpA[i])
  gpA.append(G)

G = B.copy()
gpB = [G]
for i in xrange(6):
  G = cv2.pyrDown(gpB[i])
  gpB.append(G)

lpA = [gpA[5]]
for i in xrange(5, 0, -1):
  # GE = cv2.pyrUp(gpA[i])
  size = (gpA[i-1].shape[1], gpA[i-1].shape[0])
  GE = cv2.pyrUp(gpA[i], dstsize = size)
  L = cv2.subtract(gpA[i-1], GE)
  lpA.append(L)

lpB = [gpB[5]]
for i in xrange(5, 0, -1):
  # GE = cv2.gyrUp(gpB[i])
  size = (gpB[i-1].shape[1], gpB[i-1].shape[0])
  GE = cv2.pyrUp(gpB[i], dstsize = size)
  L = cv2.subtract(gpB[i-1], GE)
  lpB.append(L)

LS = []
for la,lb in zip(lpA, lpB):
  rows, cols, dpt = la.shape
  ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
  LS.append(ls)

ls_ = LS[0]
for i in xrange(1,6):
  # ls_ = cv2.pyrUp(ls_)
  # ls_ = cv2.add(ls_, LS[i])
  size = (LS[i].shape[1], LS[i].shape[0])
  ls_ = cv2.pyrUp(ls_, dstsize = size)
  ls_ = cv2.add(ls_, LS[i])

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)

