import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]=0,255,0  #BLUE,GREEN,RED    #img[height,width]

cv2.line(img,(0,0),(300,300),(0,255,0),3)  #image,startPoint(width,height),endPoint,(B,G,R),lineWidth
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)  #image,text,startpoint,font,fontSize,color,lineWidth


cv2.imshow("image",img)

cv2.waitKey(0)