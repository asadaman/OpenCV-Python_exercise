import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.jpg')

kernerl = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img, -1, kernerl)

plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
