import matplotlib.pyplot as plt
import cv2
from skimage import filters

img = cv2.imread("/home/niyazbek/Загрузки/TrinityBikes.JPG")
image = cv2.imread("/home/niyazbek/Загрузки/TrinityBikes.JPG",0)

#finding the magnitude
edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True,
                         figsize=(8, 4))

axes[0].imshow(edge_roberts, cmap=plt.cm.gray)
axes[0].set_title('Roberts Edge Detection')

axes[1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[1].set_title('Compass Edge Detection')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

#2 ex
blur = cv2.GaussianBlur(img,(5,5),2)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

dst = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
abs_dst = cv2.convertScaleAbs(dst)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(abs_dst),plt.title('Laplace')
plt.xticks([]), plt.yticks([])
plt.show()

#3 ex
#img , thr values
edges = cv2.Canny(image,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
