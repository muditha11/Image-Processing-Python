import cv2
import numpy as np

img = cv2.imread("Resources/download.jpg")
print(img.shape)  #height,wight,Channel number

imgResize = cv2.resize(img,(200,320))
print(imgResize.shape)

imgCropped = img[50:100,150:300]

cv2.imshow("Image",img)
cv2.imshow("Resized",imgResize)
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)
