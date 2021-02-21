import cv2
import kwargs as kwargs
import noise as noise
import numpy as np
import skimage
from PIL import Image ,ImageOps
from skimage.util import random_noise

img = cv2.imread("/home/niyazbek/Загрузки/labka.jpg")
#grayscale
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow('Gray image', grayScale)
#quantise
#2
im1 = Image.open(r"/home/niyazbek/Загрузки/labka.jpg")
im2 = ImageOps.posterize(im1, 2)
im2.show()
#quintise 4 bit
#im3 = Image.open(r"/home/niyazbek/Загрузки/labka.jpg")
#im4 = ImageOps.posterize(im3, 4)
#im4.show()

#quintise 6 bit
#im3 = Image.open(r"/home/niyazbek/Загрузки/labka.jpg")
#im4 = ImageOps.posterize(im3, 6)
#im4.show()

#to see the other quantise you need to delte previous

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imwrite("yuv.png", yuv)

hls = cv2.cvtColor(img,cv2.COLOR_HLS2BGR)
cv2.imwrite("hls.png", hls)


noise_img1 = random_noise(img, mode='s&p', amount=0.3)
cv2.imshow('salt and pepper', noise_img1)

noise_img =skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True)
cv2.imshow('gaussian noises', noise_img)

blurred_2 = np.hstack([cv2.blur(img,(9,9))])
cv2.imshow('blur',blurred_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
