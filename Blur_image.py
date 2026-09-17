import numpy as np
import cv2 as cv
from matplotlib import pyplot  as plt

img = cv.imread('imagem.jpg') 
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 

Averaging_blur = cv.blur(img,(10,10))

Gaussian_blur = cv.GaussianBlur(img,(21,21), 0)

Median_blur = cv.medianBlur(img,9)

BilateralFilter_blur = cv.bilateralFilter(img,10,258,195)

plt.figure(figsize=(15, 5))

plt.subplot(1,5,1)
plt.imshow(img)
plt.title('original')


plt.subplot(1,5,2)
plt.imshow(Averaging_blur)
plt.title('Averaging')


plt.subplot(1,5,3)
plt.imshow(Gaussian_blur)
plt.title('Gaussian')

plt.subplot(1,5,4)
plt.imshow(Median_blur)
plt.title('Median')

plt.subplot(1,5,5)
plt.imshow(BilateralFilter_blur)
plt.title('Bilateral Filter')

plt.tight_layout()
plt.show()
