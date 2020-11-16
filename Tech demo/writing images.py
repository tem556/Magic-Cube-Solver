import cv2
import numpy as np
print ("PACKAGE IMPORTED")

img = cv2.imread("Resources/bruh.jpg")
print (img)
kernel = np.ones((5,5), np.uint8)
img = img[0:200, 0:320]


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilate, kernel, iterations=1)
print (cv2.waitKey(1))

cv2.imshow("just image", img)
# cv2.imshow("Gray image and bluuurrrury", imgGrayBlur)
# cv2.imshow("Deep fried memes filter", imgCanny)
# cv2.imshow("Dilated image", imgDilate)
# cv2.imshow("Eroded image", imgEroded)

