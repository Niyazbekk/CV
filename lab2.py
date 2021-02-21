# 2 channels H and S
# 180 for H plane and 256 for S plane.
import glob
import cv2

scr_img = cv2.imread('/home/niyazbek/Загрузки/labka.jpg')
hsv_conv_src = cv2.cvtColor(scr_img, cv2.COLOR_BGR2HSV)
hist_src_img = cv2.calcHist([hsv_conv_src], [0, 1], None, [180, 256], [0, 180] + [0, 256])

imdir = '/home/niyazbek/Рабочий стол/lab2/'

formats = ['png', 'jpg', 'tif', 'jpeg']
files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in formats]
images = [cv2.imread(file) for file in files]

for i in range(40):
    hsv_conv_img2 = cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV)
    hist_img1 = cv2.calcHist([hsv_conv_img2], [0, 1], None, [180, 256], [0, 180] + [0, 256])
    print(cv2.compareHist(hist_src_img, hist_img1, cv2.HISTCMP_CORREL))
