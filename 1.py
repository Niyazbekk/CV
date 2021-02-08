import cv2
import numpy as np

img = cv2.imread("/home/niyazbek/Загрузки/labka.jpg")
#grayscale
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow('Gray image', grayScale)
#quantise
#2
q = 8
quantized = img // q * q + q // 2
q = cv2.imwrite('out.jpg', quantized)
cv2.imshow('quantized image', q)

cv2.waitKey(0)
cv2.destroyAllWindows()
