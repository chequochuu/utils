import cv2
import numpy as np

path = '/Users/che/Downloads/sig.jpeg'
img = cv2.imread(path)

transparent_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pix = img[i,j]
        if pix[0] > max(pix[1], pix[2]) + 10:
            transparent_img[i][j] = list(pix) + [255]
        else:
            transparent_img[i][j] = list(pix) + [0]
        
cv2.imwrite('transparent_img.png', transparent_img)

