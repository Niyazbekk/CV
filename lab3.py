import cv2

img = cv2.imread('Users\Asus\Downloads\labka.jpg')

img = cv2.medianBlur(img,5)
th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow(th1)
cv2.imshow(th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
