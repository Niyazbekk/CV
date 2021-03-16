import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#Rotation by -15
img = cv.imread('/home/niyazbek/Загрузки/LicensePlate.jpg' , 0)
rows,cols = img.shape
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),-15,1)
dst = cv.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


#distort
for i in range(img.shape[0]):
    img[:,i] = np.roll(img[:,i], i)
plt.imshow(img)
plt.show()

#transformations
#affine
img = cv.imread('/home/niyazbek/Загрузки/LicensePlate.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[0,0],[300,0],[0,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

#perspective
pts1 = np.float32([[0,0],[300,0],[0,200],[300,200]])
pts2 = np.float32([[0,100],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


