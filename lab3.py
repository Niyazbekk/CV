import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.pyplot import axis, imshow
from pip._vendor.colorama.ansi import set_title
import numpy as np
from skimage.filters import threshold_multiotsu, threshold_otsu

img = cv.imread('/home/niyazbek/Загрузки/lab1.jpg',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

titles = ['Original Image','BINARY','Adaptive']
images = [img, thresh1 , th3]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#Semi-otsu
thresholds = threshold_multiotsu(img)
regions = np.digitize(img, bins=thresholds)
imshow(regions, cmap='jet')
set_title('Multi-Otsu result')
axis('off')
plt.subplots_adjust()

plt.show()


thresh = threshold_otsu(img)
binary = img > thresh
imshow(binary, cmap=plt.cm.gray)
set_title('Thresholded')
axis('off')
plt.subplots_adjust()

plt.show()
