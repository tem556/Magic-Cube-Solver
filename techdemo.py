import cv2
import numpy as np

# The image processor will start with the green side facing the camera
# and yellow top, then move to the orange side, the blue, then red
# Then it will capture white with green on top and then
# Yellow with blue on top


class ImageProcessing:
	def __init__(self):
		# Access the live video through the 0 or 1 channel
		self.capture = cv2.VideoCapture(1)

	# Add the lines and the circles to the image
	def addRfrnce (self):
		size = self.imgShow.shape
		# Gets the y and x coordinates of the center of that image
		pxlY, pxlX = size[0] // 2, size[1] // 2
		# Gets a reasonable side length for the square
		# Gets the length of a single cubicle
		sqrLnth = (pxlX + pxlY) // 2; cbclLnth = (sqrLnth // 3)
		# Gets the coordinates for the square (for the cube)
		pxlYStart, pxlXStart = pxlY - (sqrLnth // 2), pxlX - (sqrLnth // 2)
		pxlYEnd, pxlXEnd = pxlY + (sqrLnth // 2), pxlX + (sqrLnth // 2)
		# Makes a square, in which the user shows their cube
		cv2.rectangle(self.imgShow, (pxlXStart, pxlYStart), (pxlXEnd, pxlYEnd), (0, 0, 0), 2)
		# Has the coordinates of where the 9 cubicle are going to be
		zeroCble, frstCble = (pxlX - cbclLnth, pxlY - cbclLnth), (pxlX, pxlY - cbclLnth)
		scndCble, thrdCble = (pxlX + cbclLnth, pxlY - cbclLnth), (pxlX - cbclLnth, pxlY)
		frthCble, ffthCbld = (pxlX, pxlY), (pxlX + cbclLnth, pxlY)
		sxthCble, svthCble = (pxlX - cbclLnth, pxlY + cbclLnth), (pxlX, pxlY + cbclLnth)
		egthCble = (pxlX + cbclLnth, pxlY + cbclLnth)
		self.side = [zeroCble, frstCble, scndCble, thrdCble, frthCble]
		self.side.extend([ffthCbld, sxthCble, svthCble, egthCble])
		for i in self.side:
			img = cv2.circle(self.imgShow, i, 15, (0, 0, 0), 2)
		# Returns the image and the coordinates of the 9 circles
		return img

	# Defines the order of presenting the cube in front of camera here
	def addText(self, fSide, uSide):
		# Reminder that the y and x axis are switched for this
		size = self.imgShow.shape
		textF = "Faces the Camera: "+fSide
		textU = "Faces Upwards: "+uSide
		textKey = "Please press 'P' if finished"
		font = cv2.FONT_HERSHEY_SIMPLEX
		self.imgShow = cv2.putText(self.imgShow, textF, (0,25), font, 1, (0,0,0),2)
		self.imgShow = cv2.putText(self.imgShow, textU, (0, 75), font, 1, (0, 0, 0), 2)
		self.imgShow = cv2.putText(self.imgShow, textKey,(0, size[0]-25) , font, 1, (0, 0, 0), 2)


	# Takes the image and the coordinates as parameters
	def getColors(self,img):
		answer = []
		# Gets the mean of five point within the circle for each point
		# and adds it to the answer list
		for i in self.side:
			bluePnt=int(img[i[1], i[0]][0])
			bluePnt+=(int(img[i[1], i[0]+10][0])+int(img[i[1]+10, i[0]][0]))
			bluePnt+=(int(img[i[1], i[0]-10][0]) + int(img[i[1]-10, i[0]][0]))
			greenPnt=int(img[i[1], i[0]][1])
			greenPnt+=int(img[i[1], i[0]+10][1]) + int(img[i[1]+10, i[0]][1])
			greenPnt+=int(img[i[1], i[0]-10][1]) + int(img[i[1]-10, i[0]][1])
			redPnt=int(img[i[1], i[0]][2])
			redPnt+=int(img[i[1], i[0]+10][2]) + int(img[i[1]+10, i[0]][2])
			redPnt+=int(img[i[1], i[0]-10][2]) + int(img[i[1]-10, i[0]][2])
			bluePnt, greenPnt, redPnt = bluePnt//5, greenPnt//5, redPnt//5
			answer.append([bluePnt, greenPnt, redPnt])
		return answer

	def getAllColors(self):
		self.colorList = []
		g, o, r, b, w, y = "Green", "Orange", "Red", "Blue", "White", "Yellow"
		sidesList = [(g, y), (o, y), (b, y), (r, y), (w, g), (y, b)]
		for i in sidesList:
			condition = True
			# Goes through frames (images) that make up a video
			while condition:
				# Gets the current frame as img for getting color
				success, img = self.capture.read()
				# Get another copy of the frame for showing
				success, self.imgShow = self.capture.read()
				# Gets the size of the image
				self.addRfrnce()
				self.imgShow = cv2.flip(self.imgShow,1)
				self.addText(i[0], i[1])
				cv2.imshow("Window", self.imgShow)
				# Press (P) to print the color
				if cv2.waitKey(1) & 0xFF == ord("p"):
					self.colorList.append(self.getColors(img))
					condition = False




	# This function converts numbers into colors
	# Note:The image processor will start with the green side facing the camera
	# and yellow top, then move to the orange side, the blue, then red
	# Then it will capture white with green on top and then
	# Yellow with blue on top
	def convertColors(self):
		colorList = self.colorList
		self.answerList = []
		self.anchorList = [colorList[0][4], colorList[1][4]]
		self.anchorList.extend([colorList[2][4], colorList[3][4]])
		self.anchorList.extend([colorList[4][4], colorList[5][4]])
		for i in colorList:
			for n in i:
				minDiff = (255, ())
				for s in self.anchorList:
					bDiff = abs(n[0]-s[0])
					gDiff = abs(n[1]-s[1])
					rDiff = abs(n[2]-s[2])
					if bDiff+gDiff+rDiff<=minDiff[0]:
						minDiff = bDiff+gDiff+rDiff, s
				self.answerList.append(minDiff[1])


	def convertList(self):
		anchorList = self.anchorList
		answerList = self.answerList
		finalList = []
		gAnchor, oAnchor, bAnchor=anchorList[0], anchorList[1], anchorList[2]
		rAnchor, wAnchor, yAnchor=anchorList[3], anchorList[4], anchorList[5]
		for i in answerList:
			if i==gAnchor:
				finalList.append("g")
			if i==oAnchor:
				finalList.append("o")
			if i==bAnchor:
				finalList.append("b")
			if i==rAnchor:
				finalList.append("r")
			if i==wAnchor:
				finalList.append("w")
			if i==yAnchor:
				finalList.append("y")
		gSide,oSide,bSide=finalList[0:9],finalList[9:18],finalList[18:27]
		rSide,wSide,ySide=finalList[27:36],finalList[36:45],finalList[45:54]
		self.gSide, self.oSide, self.bSide = gSide, oSide, bSide
		self.rSide, self.wSide, self.ySide = rSide, wSide, ySide


	def getSide(self, side):
		cSide = side
		return (cSide[0]+" "+cSide[1]+" "+cSide[2]+"\n"+
		       cSide[3]+" "+cSide[4]+" "+cSide[5]+"\n"+
		       cSide[6]+" "+cSide[7]+" "+cSide[8]+"\n")

	def printCube(self):
		g,b = self.getSide(self.gSide),self.getSide(self.bSide)
		r,o = self.getSide(self.rSide), self.getSide(self.oSide)
		y,w = self.ySide, self.wSide
		# This will print the blank lines
		print (" "*5+"|"+y[0]+" "+y[1]+" "+y[2]+"\n"+
		       " "*5+"|"+y[3]+" "+y[4]+" "+y[5]+"\n"+
		       " "*5+"|"+y[6]+" "+y[7]+" "+y[8]+"\n"+
		       r[:5]+"|"+g[:5]+"|"+o[:5]+"|"+b[:5]+"|"+"\n"+
		       r[6:11]+"|"+g[6:11]+"|"+o[6:11]+"|"+b[6:11]+"|"+"\n"+
		       r[12:17]+"|"+g[12:17]+"|"+o[12:17]+"|"+b[12:17]+"|"+"\n"+
		       " "*5+"|"+w[0]+" "+w[1]+" "+w[2]+"\n"+
		       " "*5+"|"+w[3]+" "+w[4]+" "+w[5]+"\n"+
		       " "*5+"|"+w[6]+" "+w[7]+" "+w[8]+"\n")




cubeProcess = ImageProcessing()
cubeProcess.getAllColors()
cubeProcess.convertColors()
cubeProcess.convertList()
cubeProcess.printCube()

# Takes a nested list with numbers and converts it into colors
# def convertColors(list):



