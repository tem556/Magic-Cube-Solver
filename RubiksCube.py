# Has the Rubik's Cube class that makes a rubikS cube and allows
# it to move
w = "w"; y = "y"; b = "b"; g = "g"; r = "r"; o = "o"
# This is what a Rubik's Cube will look like for our program

wSide = [w, w, w,
         w, w, w,
         w, w, w]
ySide = [y, y, y,
         y, y, y,
         y, y, y]
bSide = [b, b, b,
         b, b, b,
         b, b, b]
gSide = [g, g, g,
         g, g, g,
         g, g, g]
rSide = [r, r, r,
         r, r, r,
         r, r, r]
oSide = [o, o, o,
         o, o, o,
         o, o, o]

class RubiksCube:
	def __init__(self, wSide, ySide, bSide, gSide, rSide, oSide):
		self.wSide, self.ySide = wSide, ySide
		self.bSide, self.gSide = bSide, gSide
		self.rSide, self.oSide = rSide, oSide

	def getCube(self, side):
		wSide = side
		print (wSide[0]+" "+wSide[1]+" "+wSide[2]+"\n"+
		       wSide[3]+" "+wSide[4]+" "+wSide[5]+"\n"+
		       wSide[6]+" "+wSide[7]+" "+wSide[8]+"\n")

	# Rotates a side's color clockwise
	def rotate (self, side):
		oldSide = side[:]
		side[0], side[1], side[2] = oldSide[6], oldSide[3], oldSide[0]
		side[3], side[5], side[6] = oldSide[7], oldSide[1], oldSide[8]
		side[7], side[8] = oldSide[5], oldSide[2]

	def rotatePrime (self, side):
		oldSide = side[:]
		side [0], side[1], side[2] = oldSide[2], oldSide[5], oldSide[8]
		side[3], side[5], side[6] = oldSide[1], oldSide[7], oldSide[0]
		side[7], side[8] = oldSide[3], oldSide[6]

	# Moves the right side of the cube anti-clockwise (R')
	def moveR (self):
		whiteTwo = self.wSide[2]
		whiteFive = self.wSide[5]
		whiteEight = self.wSide[8]

		self.wSide[2] = self.bSide[2]
		self.wSide[5] = self.bSide[5]
		self.wSide[8] = self.bSide[8]

		self.bSide[2] = self.ySide[6]
		self.bSide[5] = self.ySide[3]
		self.bSide[8] = self.ySide[0]

		self.ySide[6] = self.gSide[2]
		self.ySide[3] = self.gSide[5]
		self.ySide[0] = self.gSide[8]

		self.gSide[2] = whiteTwo
		self.gSide[5] = whiteFive
		self.gSide[8] = whiteEight

		self.rotate(oSide)

	# Moves the right side of the cube clockwise (R)
	def moveRPrime (self):
		whiteTwo = self.wSide[2]
		whiteFive = self.wSide[5]
		whiteEight = self.wSide[8]

		self.wSide[2] = self.gSide[2]
		self.wSide[5] = self.gSide[5]
		self.wSide[8] = self.gSide[8]

		self.gSide[2] = self.ySide[6]
		self.gSide[5] = self.ySide[3]
		self.gSide[8] = self.ySide[0]

		self.ySide[6] = self.bSide[2]
		self.ySide[3] = self.bSide[5]
		self.ySide[0] = self.bSide[8]

		self.bSide[2] = whiteTwo
		self.bSide[5] = whiteFive
		self.bSide[8] = whiteEight

		self.rotatePrime(oSide)
		
	def moveL (self):
		whiteZero = self.wSide[0]
		whiteThree = self.wSide[3]
		whiteSix = self.wSide[6]

		self.wSide[0] = self.gSide[0]
		self.wSide[3] = self.gSide[3]
		self.wSide[6] = self.gSide[6]

		self.gSide[0] = self.ySide[8]
		self.gSide[3] = self.ySide[5]
		self.gSide[6] = self.ySide[2]

		self.ySide[8] = self.bSide[0]
		self.ySide[5] = self.bSide[3]
		self.ySide[2] = self.bSide[6]

		self.bSide[0] = whiteZero
		self.bSide[3] = whiteThree
		self.bSide[6] = whiteSix

		self.rotate(rSide)
		
	def moveLPrime(self):
		whiteTwo = self.wSide[0]
		whiteFive = self.wSide[3]
		whiteEight = self.wSide[6]

		self.wSide[0] = self.bSide[0]
		self.wSide[3] = self.bSide[3]
		self.wSide[6] = self.bSide[6]

		self.bSide[0] = self.ySide[8]
		self.bSide[3] = self.ySide[5]
		self.bSide[6] = self.ySide[2]

		self.ySide[8] = self.gSide[0]
		self.ySide[5] = self.gSide[3]
		self.ySide[2] = self.gSide[6]

		self.gSide[0] = whiteTwo
		self.gSide[3] = whiteFive
		self.gSide[6] = whiteEight

		self.rotatePrime(rSide)
		

	def moveUPrime (self):
		whiteZero = self.wSide[0]
		whiteOne = self.wSide[1]
		whiteTwo = self.wSide[2]

		self.wSide[0] = self.rSide[0]
		self.wSide[1] = self.rSide[1]
		self.wSide[2] = self.rSide[2]

		self.rSide[0] = self.ySide[0]
		self.rSide[1] = self.ySide[1]
		self.rSide[2] = self.ySide[2]

		self.ySide[0] = self.oSide[0]
		self.ySide[1] = self.oSide[1]
		self.ySide[2] = self.oSide[2]

		self.oSide[0] = whiteZero
		self.oSide[1] = whiteOne
		self.oSide[2] = whiteTwo

		self.rotatePrime(gSide)
	def moveU(self):
		whiteZero = self.wSide[0]
		whiteOne = self.wSide[1]
		whiteTwo = self.wSide[2]

		self.wSide[0] = self.oSide[0]
		self.wSide[1] = self.oSide[1]
		self.wSide[2] = self.oSide[2]

		self.oSide[0] = self.ySide[0]
		self.oSide[1] = self.ySide[1]
		self.oSide[2] = self.ySide[2]

		self.ySide[0] = self.rSide[0]
		self.ySide[1] = self.rSide[1]
		self.ySide[2] = self.rSide[2]

		self.rSide[0] = whiteZero
		self.rSide[1] = whiteOne
		self.rSide[2] = whiteTwo

		self.rotate(gSide)

	def moveDPrime (self):
		whiteSix = self.wSide[6]
		whiteSeven = self.wSide[7]
		whiteEight = self.wSide[8]

		self.wSide[6] = self.oSide[6]
		self.wSide[7] = self.oSide[7]
		self.wSide[8] = self.oSide[8]

		self.oSide[6] = self.ySide[6]
		self.oSide[7] = self.ySide[7]
		self.oSide[8] = self.ySide[8]

		self.ySide[6] = self.rSide[6]
		self.ySide[7] = self.rSide[7]
		self.ySide[8] = self.rSide[8]

		self.rSide[6] = whiteSix
		self.rSide[7] = whiteSeven
		self.rSide[8] = whiteEight

		self.rotatePrime(bSide)

	def moveD (self):
		whiteSix = self.wSide[6]
		whiteSeven = self.wSide[7]
		whiteEight = self.wSide[8]

		self.wSide[6] = self.rSide[6]
		self.wSide[7] = self.rSide[7]
		self.wSide[8] = self.rSide[8]

		self.rSide[6] = self.ySide[6]
		self.rSide[7] = self.ySide[7]
		self.rSide[8] = self.ySide[8]

		self.ySide[6] = self.oSide[6]
		self.ySide[7] = self.oSide[7]
		self.ySide[8] = self.oSide[8]

		self.oSide[6] = whiteSix
		self.oSide[7] = whiteSeven
		self.oSide[8] = whiteEight

		self.rotate(bSide)

	def moveFPrime (self):

		greenSix = self.gSide[6]
		greenSeven = self.gSide[7]
		greenEight = self.gSide[8]

		self.gSide[6] = self.oSide[0]
		self.gSide[7] = self.oSide[3]
		self.gSide[8] = self.oSide[6]

		self.oSide[0] = self.bSide[2]
		self.oSide[3] = self.bSide[1]
		self.oSide[6] = self.bSide[0]

		self.bSide[0] = self.rSide[2]
		self.bSide[1] = self.rSide[5]
		self.bSide[2] = self.rSide[8]

		self.rSide[2] = greenEight
		self.rSide[5] = greenSeven
		self.rSide[8] = greenSix

		self.rotatePrime(wSide)

	def moveF (self):
		greenSix = self.gSide[6]
		greenSeven = self.gSide[7]
		greenEight = self.gSide[8]

		self.gSide[6] = self.rSide[8]
		self.gSide[7] = self.rSide[5]
		self.gSide[8] = self.rSide[2]

		self.rSide[2] = self.bSide[0]
		self.rSide[5] = self.bSide[1]
		self.rSide[8] = self.bSide[2]

		self.bSide[0] = self.oSide[6]
		self.bSide[1] = self.oSide[3]
		self.bSide[2] = self.oSide[0]

		self.oSide[0] = greenSix
		self.oSide[3] = greenSeven
		self.oSide[6] = greenEight

		self.rotate(wSide)

	def moveBPrime (self):
		greenZero = self.gSide[0]
		greenOne = self.gSide[1]
		greenTwo = self.gSide[2]

		self.gSide[0] = self.rSide[6]
		self.gSide[1] = self.rSide[3]
		self.gSide[2] = self.rSide[0]

		self.rSide[0] = self.bSide[6]
		self.rSide[3] = self.bSide[7]
		self.rSide[6] = self.bSide[8]

		self.bSide[6] = self.oSide[8]
		self.bSide[7] = self.oSide[5]
		self.bSide[8] = self.oSide[2]

		self.oSide[2] = greenZero
		self.oSide[5] = greenOne
		self.oSide[8] = greenTwo

		self.rotatePrime(ySide)

	def moveB (self):
		greenZero = self.gSide[0]
		greenOne = self.gSide[1]
		greenTwo = self.gSide[2]

		self.gSide[0] = self.oSide[2]
		self.gSide[1] = self.oSide[5]
		self.gSide[2] = self.oSide[8]

		self.oSide[2] = self.bSide[8]
		self.oSide[5] = self.bSide[7]
		self.oSide[8] = self.bSide[6]

		self.bSide[6] = self.rSide[0]
		self.bSide[7] = self.rSide[3]
		self.bSide[8] = self.rSide[6]

		self.rSide[0] =greenTwo
		self.rSide[3] = greenOne
		self.rSide[6] = greenZero

		self.rotate(ySide)











cube = RubiksCube(wSide,ySide, bSide, gSide, rSide, oSide)
cube.moveU()
cube.moveLPrime()
cube.moveB()
cube.moveD()
cube.moveUPrime()
cube.moveRPrime()
cube.moveBPrime()
cube.moveUPrime()
cube.getCube(rSide)


		
		
		
		
		
		
		
		
		
		