import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def segmentation(image, technique):
	if technique == 'THRESH_BINARY':
		ret,thresh1 = cv.threshold(img,100,200,cv.THRESH_BINARY)
		return thresh1
	if technique == 'THRESH_BINARY_INV':
		ret,thresh2 = cv.threshold(img,100,200,cv.THRESH_BINARY_INV)
		return thresh2
	if technique == 'THRESH_TRUNC':
		ret,thresh3 = cv.threshold(img,100,200,cv.THRESH_TRUNC)
		return thresh3
	if technique == 'THRESH_TOZERO':
		ret,thresh4 = cv.threshold(img,100,200,cv.THRESH_TOZERO)
		return thresh4
	if technique == 'THRESH_TOZERO_INV':
		ret,thresh5 = cv.threshold(img,100,200,cv.THRESH_TOZERO_INV)
		return thresh5

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

if __name__ == '__main__':
    path = './static'
    positives = os.listdir(path)
    for name in positives:
        image_path = os.path.join(path, name)
        image = cv2.imread(image_path)
        output = segmentation(image, 'THRESH_BINARY_INV')
        print('[output]\n', output)
