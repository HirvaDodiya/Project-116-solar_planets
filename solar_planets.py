import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,"Mercury",(110,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(285,270),cv2.FONT_HERSHEY_COMPLEX,0.50,(255,255,255))
cv2.putText(img,"Mars",(380,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(480,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(770,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1120,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("Output",img)
cv2.waitKey(0)