from RubiksCube import *

w = "w"; y = "y"; b = "b"; g = "g"; r = "r"; o = "o"

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

class Solver:
	def __init__(self, wSide, ySide, bSide, gSide, rSide, oSide ):
		self.cube = RubikCube(wSide, ySide, bSide, gSide, rSide, oSide)



	def doStuff(self):
		self.cube.move(["R"])
		self.cube.printCube()



solution = Solver(wSide, ySide, bSide, gSide, rSide, oSide)
solution.doStuff()

