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

class RubikCube:
	def __init__(self, wSide, ySide, bSide, gSide, rSide, oSide):
		self.wSide, self.ySide = wSide, ySide
		self.bSide, self.gSide = bSide, gSide
		self.rSide, self.oSide = rSide, oSide


	def getSide(self, side):
		cSide = side
		return (cSide[0]+" "+cSide[1]+" "+cSide[2]+"\n"+
		       cSide[3]+" "+cSide[4]+" "+cSide[5]+"\n"+
		       cSide[6]+" "+cSide[7]+" "+cSide[8]+"\n")

	# Prints the sides, has white as the middle
	def printCube(self):
		g,b = self.getSide(gSide),self.getSide(bSide)
		r,o = self.getSide(rSide), self.getSide(oSide)
		y,w = self.getSide(ySide), self.getSide(wSide)
		# This will print the blank lines
		print (" "*5+"|"+ySide[0]+" "+ySide[1]+" "+ySide[2]+"\n"+
		       " "*5+"|"+ySide[3]+" "+ySide[4]+" "+ySide[5]+"\n"+
		       " "*5+"|"+ySide[6]+" "+ySide[7]+" "+ySide[8]+"\n"+
		       r[:5]+"|"+g[:5]+"|"+o[:5]+"|"+b[:5]+"|"+"\n"+
		       r[6:11]+"|"+g[6:11]+"|"+o[6:11]+"|"+b[6:11]+"|"+"\n"+
		       r[12:17]+"|"+g[12:17]+"|"+o[12:17]+"|"+b[12:17]+"|"+"\n"+
		       " "*5+"|"+wSide[0]+" "+wSide[1]+" "+wSide[2]+"\n"+
		       " "*5+"|"+wSide[3]+" "+wSide[4]+" "+wSide[5]+"\n"+
		       " "*5+"|"+wSide[6]+" "+wSide[7]+" "+wSide[8]+"\n")
		       
		       


	# Rotates a side's color clockwise
	# Used when a move is made to a certain side
	# That side's color also rotate
	def rotate (self, side):
		oldSide = side[:]
		side[0], side[1], side[2] = oldSide[6], oldSide[3], oldSide[0]
		side[3], side[5], side[6] = oldSide[7], oldSide[1], oldSide[8]
		side[7], side[8] = oldSide[5], oldSide[2]

	# Rotates a side's color anti-clockwise
	def rotatePrime (self, side):
		oldSide = side[:]
		side [0], side[1], side[2] = oldSide[2], oldSide[5], oldSide[8]
		side[3], side[5], side[6] = oldSide[1], oldSide[7], oldSide[0]
		side[7], side[8] = oldSide[3], oldSide[6]

	# Moves the right side of the cube clockwise (R)
	def moveR (self):
		# Saves this side's color temporarily
		whiteTwo = self.wSide[2]
		whiteFive = self.wSide[5]
		whiteEight = self.wSide[8]
		# "Shifts" each color to its desired position

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

	# Moves the right side of the cube anti-clockwise (R')
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

	# Moves the left side of the cube clockwise
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

	# Moves the left side of the cube anti-clockwise
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
		
	# Moves the upper side of the cube anti-clockwise(<--from that side's perspective)
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

	# Moves the upper side clockwise
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

	# Moves the down side(bottom row) anti-clockwise
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

	# Moves the down side of the cube clockwise
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

	# Moves the front side of the cube anti-clockwise
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

	# Moves the front side of the cube clockwise
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

	# Moves the back side of the cube anti-clockwise
	# Keep in mind that the indices for the back side are flipped
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

	# Moves the back side of the cube clockwise
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

	# Takes a list with required moves and performs them
	# using the functions above.

	def move(self, list):
		# Base case: when the list is empty
		if list==[]:return True
		elif list[0]=="R":self.moveR()
		elif list[0]=="R'":self.moveRPrime()
		elif list[0]=="L":self.moveL()
		elif list[0]=="L'":self.moveLPrime()
		elif list[0]=="U":self.moveU()
		elif list[0]=="U'":self.moveUPrime()
		elif list[0]=="D":self.moveD()
		elif list[0]=="D'":self.moveDPrime()
		elif list[0]=="F":self.moveF()
		elif list[0]=="F'":self.moveFPrime()
		elif list[0]=="B": self.moveB()
		elif list[0]=="B'":self.moveBPrime()
		# If a wrong move (not recognizable character) is inputted :
		else: print ("Invalid move")
		self.move(list[1:])





# This list takes the user commands in a list
# Possible commands are:
# R and R' : moves the right side clockwise, prime moves it anti-clockwise
# L and L' : moves the left side...
# U and U' : moves the upper column...
# D and D' : moves the bottom column(down)...
# F and F' : moves the front side...
# B and B' : moves the back side...
# Example:
cube = RubikCube(wSide, ySide, bSide, gSide, rSide, oSide)
# cube.move(["R","F", "U","U'","F'","R'"])
# # Print all six sides of the cube
cube.printCube()


		
		
		
		
		
		
		
		
		
		