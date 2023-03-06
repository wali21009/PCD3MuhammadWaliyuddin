# import packages
import cv2
import imutils
import numpy as np

img1 = cv2.imread("image/city1.jpeg")
img1 = cv2.resize(img1, (600,360))
img2 = cv2.imread("image/city2.jpeg")
img2 = cv2.resize(img2, (600,360))

#grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2  = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#absdiff
diff = cv2.absdiff(gray1, gray2)
cv2.imshow("diff(img1, img2)", diff)

#threshold
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#cv2.imshow("Threshold", thresh)

#dilation
kernel = np.ones((5,5), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations=2)
cv2.imshow("Dilation", dilate)

#find countours
contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

#loop
for contour in contours :
    if cv2.contourArea(contour) > 100:
        x, y, w, h=cv2.boundingRect(contour)
        cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255), 2)
#show difference
x = np.zeros((360,10,3), np.uint8)
result = np.hstack((img1, x, img2))
cv2.imshow("Difference", result)
#cv2.imshow("original City", img1)
#cv2.imshow("edited", img2)

cv2.waitKey(0)
cv2.destroyAllwindows()

