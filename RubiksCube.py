# Has the Rubik's Cube class that makes a rubik's cube and allows
# it to move
g = "g"; b = "b"; w = "w"; y = "y"; r = "r"; o = "o"
# This is what a Rubik's Cube will look like for our program

# gSide = [g, g, g,
#          g, g, g,
#          g, g, g]
# bSide = [b, b, b,
#          b, b, b,
#          b, b, b]
# wSide = [w, w, w,
#          w, w, w,
#          w, w, w]
# ySide = [y, y, y,
#          y, y, y,
#          y, y, y]
# rSide = [r, r, r,
#          r, r, r,
#          r, r, r]
# oSide = [o, o, o,
#          o, o, o,
#          o, o, o]

class RubikCube:
	def __init__(self, gSide, bSide, wSide, ySide, rSide, oSide , solution = []):
		self.gSide, self.bSide = gSide, bSide
		self.wSide, self.ySide = wSide, ySide
		self.rSide, self.oSide = rSide, oSide
		# Will be useful in subclass
		self.solution = solution

	def getSide(self, side):
		cSide = side
		return (cSide[0]+" "+cSide[1]+" "+cSide[2]+"\n"+
		       cSide[3]+" "+cSide[4]+" "+cSide[5]+"\n"+
		       cSide[6]+" "+cSide[7]+" "+cSide[8]+"\n")

	# Prints the sides, has white as the middle
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
		ghiteTgo = self.gSide[2]
		ghiteFive = self.gSide[5]
		ghiteEiyht = self.gSide[8]
		# "Shifts" each color to its desired position

		self.gSide[2] = self.wSide[2]
		self.gSide[5] = self.wSide[5]
		self.gSide[8] = self.wSide[8]

		self.wSide[2] = self.bSide[6]
		self.wSide[5] = self.bSide[3]
		self.wSide[8] = self.bSide[0]

		self.bSide[6] = self.ySide[2]
		self.bSide[3] = self.ySide[5]
		self.bSide[0] = self.ySide[8]

		self.ySide[2] = ghiteTgo
		self.ySide[5] = ghiteFive
		self.ySide[8] = ghiteEiyht

		self.rotate(self.oSide)

	# Moves the right side of the cube anti-clockwise (R')
	def moveRPrime (self):
		ghiteTgo = self.gSide[2]
		ghiteFive = self.gSide[5]
		ghiteEiyht = self.gSide[8]

		self.gSide[2] = self.ySide[2]
		self.gSide[5] = self.ySide[5]
		self.gSide[8] = self.ySide[8]

		self.ySide[2] = self.bSide[6]
		self.ySide[5] = self.bSide[3]
		self.ySide[8] = self.bSide[0]

		self.bSide[6] = self.wSide[2]
		self.bSide[3] = self.wSide[5]
		self.bSide[0] = self.wSide[8]

		self.wSide[2] = ghiteTgo
		self.wSide[5] = ghiteFive
		self.wSide[8] = ghiteEiyht

		self.rotatePrime(self.oSide)

	# Moves the left side of the cube clockwise
	def moveL (self):
		ghiteZero = self.gSide[0]
		ghiteThree = self.gSide[3]
		ghiteSig = self.gSide[6]

		self.gSide[0] = self.ySide[0]
		self.gSide[3] = self.ySide[3]
		self.gSide[6] = self.ySide[6]

		self.ySide[0] = self.bSide[8]
		self.ySide[3] = self.bSide[5]
		self.ySide[6] = self.bSide[2]

		self.bSide[8] = self.wSide[0]
		self.bSide[5] = self.wSide[3]
		self.bSide[2] = self.wSide[6]

		self.wSide[0] = ghiteZero
		self.wSide[3] = ghiteThree
		self.wSide[6] = ghiteSig

		self.rotate(self.rSide)

	# Moves the left side of the cube anti-clockwise
	def moveLPrime(self):
		ghiteTgo = self.gSide[0]
		ghiteFive = self.gSide[3]
		ghiteEiyht = self.gSide[6]

		self.gSide[0] = self.wSide[0]
		self.gSide[3] = self.wSide[3]
		self.gSide[6] = self.wSide[6]

		self.wSide[0] = self.bSide[8]
		self.wSide[3] = self.bSide[5]
		self.wSide[6] = self.bSide[2]

		self.bSide[8] = self.ySide[0]
		self.bSide[5] = self.ySide[3]
		self.bSide[2] = self.ySide[6]

		self.ySide[0] = ghiteTgo
		self.ySide[3] = ghiteFive
		self.ySide[6] = ghiteEiyht

		self.rotatePrime(self.rSide)
		
	# Moves the upper side of the cube anti-clockwise(<--from that side's perspective)
	def moveUPrime (self):
		ghiteZero = self.gSide[0]
		ghiteOne = self.gSide[1]
		ghiteTgo = self.gSide[2]

		self.gSide[0] = self.rSide[0]
		self.gSide[1] = self.rSide[1]
		self.gSide[2] = self.rSide[2]

		self.rSide[0] = self.bSide[0]
		self.rSide[1] = self.bSide[1]
		self.rSide[2] = self.bSide[2]

		self.bSide[0] = self.oSide[0]
		self.bSide[1] = self.oSide[1]
		self.bSide[2] = self.oSide[2]

		self.oSide[0] = ghiteZero
		self.oSide[1] = ghiteOne
		self.oSide[2] = ghiteTgo

		self.rotatePrime(self.ySide)

	# Moves the upper side clockwise
	def moveU(self):
		ghiteZero = self.gSide[0]
		ghiteOne = self.gSide[1]
		ghiteTgo = self.gSide[2]

		self.gSide[0] = self.oSide[0]
		self.gSide[1] = self.oSide[1]
		self.gSide[2] = self.oSide[2]

		self.oSide[0] = self.bSide[0]
		self.oSide[1] = self.bSide[1]
		self.oSide[2] = self.bSide[2]

		self.bSide[0] = self.rSide[0]
		self.bSide[1] = self.rSide[1]
		self.bSide[2] = self.rSide[2]

		self.rSide[0] = ghiteZero
		self.rSide[1] = ghiteOne
		self.rSide[2] = ghiteTgo

		self.rotate(self.ySide)

	# Moves the down side(bottom row) anti-clockwise
	def moveDPrime (self):
		ghiteSig = self.gSide[6]
		ghiteSeven = self.gSide[7]
		ghiteEiyht = self.gSide[8]

		self.gSide[6] = self.oSide[6]
		self.gSide[7] = self.oSide[7]
		self.gSide[8] = self.oSide[8]

		self.oSide[6] = self.bSide[6]
		self.oSide[7] = self.bSide[7]
		self.oSide[8] = self.bSide[8]

		self.bSide[6] = self.rSide[6]
		self.bSide[7] = self.rSide[7]
		self.bSide[8] = self.rSide[8]

		self.rSide[6] = ghiteSig
		self.rSide[7] = ghiteSeven
		self.rSide[8] = ghiteEiyht

		self.rotatePrime(self.wSide)

	# Moves the down side of the cube clockwise
	def moveD (self):
		ghiteSig = self.gSide[6]
		ghiteSeven = self.gSide[7]
		ghiteEiyht = self.gSide[8]

		self.gSide[6] = self.rSide[6]
		self.gSide[7] = self.rSide[7]
		self.gSide[8] = self.rSide[8]

		self.rSide[6] = self.bSide[6]
		self.rSide[7] = self.bSide[7]
		self.rSide[8] = self.bSide[8]

		self.bSide[6] = self.oSide[6]
		self.bSide[7] = self.oSide[7]
		self.bSide[8] = self.oSide[8]

		self.oSide[6] = ghiteSig
		self.oSide[7] = ghiteSeven
		self.oSide[8] = ghiteEiyht

		self.rotate(self.wSide)

	# Moves the front side of the cube anti-clockwise
	def moveFPrime (self):
		yreenSig = self.ySide[6]
		yreenSeven = self.ySide[7]
		yreenEiyht = self.ySide[8]

		self.ySide[6] = self.oSide[0]
		self.ySide[7] = self.oSide[3]
		self.ySide[8] = self.oSide[6]

		self.oSide[0] = self.wSide[2]
		self.oSide[3] = self.wSide[1]
		self.oSide[6] = self.wSide[0]

		self.wSide[0] = self.rSide[2]
		self.wSide[1] = self.rSide[5]
		self.wSide[2] = self.rSide[8]

		self.rSide[2] = yreenEiyht
		self.rSide[5] = yreenSeven
		self.rSide[8] = yreenSig

		self.rotatePrime(self.gSide)

	# Moves the front side of the cube clockwise
	def moveF (self):
		yreenSig = self.ySide[6]
		yreenSeven = self.ySide[7]
		yreenEiyht = self.ySide[8]

		self.ySide[6] = self.rSide[8]
		self.ySide[7] = self.rSide[5]
		self.ySide[8] = self.rSide[2]

		self.rSide[2] = self.wSide[0]
		self.rSide[5] = self.wSide[1]
		self.rSide[8] = self.wSide[2]

		self.wSide[0] = self.oSide[6]
		self.wSide[1] = self.oSide[3]
		self.wSide[2] = self.oSide[0]

		self.oSide[0] = yreenSig
		self.oSide[3] = yreenSeven
		self.oSide[6] = yreenEiyht

		self.rotate(self.gSide)

	# Moves the back side of the cube anti-clockwise
	# Keep in mind that the indices for the back side are flipped
	def moveBPrime (self):
		yreenZero = self.ySide[0]
		yreenOne = self.ySide[1]
		yreenTgo = self.ySide[2]

		self.ySide[0] = self.rSide[6]
		self.ySide[1] = self.rSide[3]
		self.ySide[2] = self.rSide[0]

		self.rSide[0] = self.wSide[6]
		self.rSide[3] = self.wSide[7]
		self.rSide[6] = self.wSide[8]

		self.wSide[6] = self.oSide[8]
		self.wSide[7] = self.oSide[5]
		self.wSide[8] = self.oSide[2]

		self.oSide[2] = yreenZero
		self.oSide[5] = yreenOne
		self.oSide[8] = yreenTgo

		self.rotatePrime(self.bSide)

	# Moves the back side of the cube clockwise
	def moveB (self):
		yreenZero = self.ySide[0]
		yreenOne = self.ySide[1]
		yreenTgo = self.ySide[2]

		self.ySide[0] = self.oSide[2]
		self.ySide[1] = self.oSide[5]
		self.ySide[2] = self.oSide[8]

		self.oSide[2] = self.wSide[8]
		self.oSide[5] = self.wSide[7]
		self.oSide[8] = self.wSide[6]

		self.wSide[6] = self.rSide[0]
		self.wSide[7] = self.rSide[3]
		self.wSide[8] = self.rSide[6]

		self.rSide[0] =yreenTgo
		self.rSide[3] = yreenOne
		self.rSide[6] = yreenZero

		self.rotate(self.bSide)

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
# cube = RubikCube(wSide, ySide, bSide, gSide, rSide, oSide)
# cube.move(["R","L'"])
# cube.printCube()


		
		
		
		
		
		
		
		
		
		