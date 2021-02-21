#2 channels H and S
# 180 for H plane and 256 for S plane.
import glob
import cv2
imdir = '/home/niyazbek/Загрузки/'
ext = ['png', 'jpg', 'tif']    # Add image formats here
files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
images = [cv2.imread(file) for file in files]

scr_img = cv2.imread("/home/niyazbek/Загрузки/labka.jpg")
img2 = cv2.imread("/home/niyazbek/Загрузки/yuv.png")
img3 = cv2.imread("/home/niyazbek/Загрузки/result.tif")
hsv_conv_src = cv2.cvtColor(scr_img, cv2.COLOR_BGR2HSV)
hsv_conv_img2 = cv2.cvtColor(images[1], cv2.COLOR_BGR2HSV)
hsv_conv_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

hist_src_img = cv2.calcHist([hsv_conv_src], [0, 1], None, [180, 256], [0, 180] + [0, 256])
#cv2.imshow("Image1", hist_base)

hist_img1 = cv2.calcHist([hsv_conv_img2], [0, 1], None, [180, 256], [0, 180] + [0, 256])
#cv2.imshow("Image2", hist_test1)

hist_img2 = cv2.calcHist([hsv_conv_img3], [0, 1], None, [180, 256], [0, 180] + [0, 256])
#cv2.imshow("Image3", hist_test2)

base_base = cv2.compareHist(hist_src_img, hist_src_img, cv2.HISTCMP_CORREL)
base_test1 = cv2.compareHist(hist_src_img, hist_img1, cv2.HISTCMP_CORREL)
base_test2 = cv2.compareHist(hist_src_img, hist_img2, cv2.HISTCMP_CORREL)
print('Method:', 'Correl ', 'Perfect , Base-Test(1), Base-Test(2) :',\
        base_base, '/', base_test1, '/', base_test2)

cv2.waitKey(0)
cv2.destroyAllWindows()
