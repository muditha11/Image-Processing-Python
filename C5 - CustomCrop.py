import cv2
import numpy as np

img = cv2.imread("Resources/kings.png")

width,height = 250,350
pts1 = np.float32([[76,377],[254,275],[147,95],[4,156]])
pts2 = np.float32([[0,height],[width,height],[width,0],[0,0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("kings",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)