import cv2
import numpy as np

image = cv2.imread("yellow_detect.jpeg")

############  Creating Color Mask ################
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([10, 120, 64])        #HSV values for Yellow color
upper_yellow = np.array([70, 224, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
res = cv2.bitwise_and(image, image, mask=mask)

############  Centroid Detection #################

M = cv2.moments(mask)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

print(cX,cY)

##########  Displaying Image ##############
# cv2.circle(res, (cX, cY), 5, (255, 255, 255), -1)
# cv2.putText(res, "("+str(cX)+","+str(cY)+")", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
# imS = cv2.resize(res, (640, 520))
# cv2.imshow("Image", imS)
# cv2.waitKey(0)







