import cv2
import numpy as np
# Access the live video through the 1 channel
capture = cv2.VideoCapture(0)

condition = True
# Goes through frames (images) that make up a video
while condition:
	# Gets the current frame as img for getting color
	success, img = capture.read()
	# Get another copy of the frame for showing
	success, imgShow = capture.read()
	# Gets the size of the image
	size = img.shape
	imgShow = cv2.cvtColor(imgShow, cv2.COLOR_BGR2HSV)
	# Gets the y and x coordinates of the center of that image
	pixely, pixelx = size[0]//2, size[1]//2
	# Adds the cross to imgShow and gets the color of original img
	imgShow[pixely-5:pixely+5,pixelx]=0,0,0
	imgShow[pixely,pixelx-5:pixelx+5]=0,0,0
	cv2.imshow("Window", imgShow)
	# Press (P) to print the color
	if cv2.waitKey(1) & 0xFF == ord("p"):
		print(img[pixely, pixelx])