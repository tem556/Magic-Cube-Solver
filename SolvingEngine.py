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

class SolveCross(RubikCube):
	# Function that shortens the solution, As the AI isn't always smart
	# it can include longer moves for doing the same task, this function
	# cancels those moves and shortens the solution
	def getSolution (self):
		sol = self.solution
		# Is used if the same move appears three consecutive time
		# Turns them into one move with opposite direction
		for i in range(2, len(sol)):
			if sol[i]==sol[i-1] and sol[i-1]==sol[i-2]:
				sol[i] = "X"
				sol[i-1] = "X"
				if "'" in sol[i]:
					sol[i-2] = sol[i-2][:1]
				else:
					sol[i-2] = sol[i-2] + "'"
		# Is used when the same move appears four times, deletes them
		for i in range (3, len(sol)):
			if sol[i]==sol[i-1] and sol[i-1]==sol[i-2] and sol[i-2]==sol[i-3]:
				sol[i], sol[i-1], sol[i-2], sol[i-3] = "X", "X", "X", "X"

		# Is used when a move and their opposite direction move appear
		# consecutively, deletes them
		for i in range(1, len(sol)):
			if sol[i]==sol[i-1]+"'" or sol[i-1]==sol[i]+"'":
				sol[i], sol[i-1] = "X", "X"
		# "Deleted" moves were converted into X's before, now will be deleted
		while "X" in sol:
			sol.remove("X")
		return sol

	# Function that translates the instructions for solving cube
	# in case the cube is rotated left, Used for reusing solve green
	# white cross function for other sides as well (for red side)
	def translateLeft(self, list):
		if list == []:
			return []
		if list[0]=="F": return ["L"] + self.translateLeft(list[1:])
		if list[0]=="F'": return ["L'"] + self.translateLeft(list[1:])
		if list[0]=="R": return ["F"] + self.translateLeft(list[1:])
		if list[0]=="R'": return ["F'"] + self.translateLeft(list[1:])
		if list[0]=="L": return ["B"] + self.translateLeft(list[1:])
		if list[0]=="L'": return ["B'"] + self.translateLeft(list[1:])
		if list[0]=="B": return  ["R"] + self.translateLeft(list[1:])
		if list[0]=="B'": return ["R'"] + self.translateLeft(list[1:])
		if list[0]=="D" or list[0]=="D'":
			return [list[0]]+ self.translateLeft(list[1:])
		if list[0]=="U" or list[0]=="U'":
			return[list[0]]+self.translateLeft(list[1:])


	# Same as above, only if rotated right (orange side)
	def translateRight(self, list):
		if list == []:
			return []
		if list[0]=="F": return ["R"] + self.translateRight(list[1:])
		if list[0]=="F'": return ["R'"]+ self.translateRight(list[1:])
		if list[0]=="R": return ["B"]+ self.translateRight(list[1:])
		if list[0]=="R'": return ["B'"]+ self.translateRight(list[1:])
		if list[0]=="L": return ["F"]+ self.translateRight(list[1:])
		if list[0]=="L'": return ["F'"]+ self.translateRight(list[1:])
		if list[0]=="B": return  ["L"]+ self.translateRight(list[1:])
		if list[0]=="B'": return ["L'"]+ self.translateRight(list[1:])
		if list[0] == "D" or list[0] == "D'":
			return [list[0]] + self.translateRight(list[1:])
		if list[0] == "U" or list[0] == "U'":
			return [list[0]] + self.translateRight(list[1:])

	# Used if the cube is rotated 180 degrees, (blue side)
	def translateBack(self, list):
		if list == []:
			return []
		if list[0]=="F": return ["B"] + self.translateBack(list[1:])
		if list[0]=="F'": return ["B'"]+ self.translateBack(list[1:])
		if list[0]=="R": return ["L"]+ self.translateBack(list[1:])
		if list[0]=="R'": return ["L'"]+ self.translateBack(list[1:])
		if list[0]=="L": return ["R"]+ self.translateBack(list[1:])
		if list[0]=="L'": return ["R'"]+ self.translateBack(list[1:])
		if list[0]=="B": return  ["F"]+ self.translateBack(list[1:])
		if list[0]=="B'": return ["F'"]+ self.translateBack(list[1:])
		if list[0] == "D" or list[0] == "D'":
			return [list[0]] + self.translateBack(list[1:])
		if list[0] == "U" or list[0] == "U'":
			return [list[0]] + self.translateBack(list[1:])





	# Has the solution if the white green cubicle for cross
	# is in the yellow side, gets the solution by extending solution list
	# And then executes them to see the next course of action
	def whiteY(self, wSide, ySide, frontSide, backSide, rightSide, leftSide, color):
		sol = []
		if wSide[1]=="w" and frontSide[7]==color:
			sol.extend([])
		elif ySide[7]=="w" and frontSide[1]==color:
			sol.extend(["F", "F"])
		elif ySide[7]==color and frontSide[1]=="w":
			sol.extend(["U'", "R'", "F", "R"])
		elif ySide[5]=="w" and rightSide[1]==color:
			sol.extend(["U", "F", "F"])
		elif ySide[5] == color and rightSide[1] == "w":
			sol.extend(["R'", "F", "R"])
		elif ySide[3]=="w" and leftSide[1]==color:#################
			sol.extend(["U'", "F", "F"])
		elif ySide[3]==color and leftSide[1]=="w":
			sol.extend(["L", "F'", "L'"])
		elif ySide[1]=="w" and backSide[1]==color:
			sol.extend(["U", "U", "F", "F"])
		elif ySide[1]==color and backSide[1]=="w":
			sol.extend(["U", "R'", "F", "R"])
		return sol
	# Same as above, just for the white side
	def whiteW(self, wSide,frontSide, backSide, rightSide, leftSide, color):
		sol = []
		if wSide[1]=="w" and frontSide[7]==color:
			sol.extend([])
		elif wSide[3]=="w" and leftSide[7]==color:
			sol.extend(["L", "L", "U'", "F", "F"])
		elif wSide[5]=="w" and rightSide[7]==color:
			sol.extend(["R", "R", "U", "F", "F"])
		elif wSide[7]=="w" and backSide[7]==color:
			sol.extend(["B", "B", "U", "U", "F", "F"])
		elif wSide[1]==color and frontSide[7]=="w":
			sol.extend(["F'", "D'", "L", "D"])
		elif wSide[3]==color and leftSide[7]=="w":
			sol.extend(["L'", "F'", "L"])
		elif wSide[5]==color and rightSide[7]=="w":
			sol.extend(["R", "F"])
		elif wSide[7]==color and backSide[7]=="w":
			sol.extend(["B","R'","U", "R", "F", "F"])
		return sol
	# Same as above, but for rest of sides
	def white(self, wSide,frontSide, backSide, rightSide, leftSide, color):
		sol = []
		if wSide[1] == "w" and frontSide[7] == color:
			sol.extend([])
		elif frontSide[5]==color and rightSide[3]=="w":
			sol.extend(["F"])
		elif   frontSide[3]==color and leftSide[5] =="w":
			sol.extend(["F'"])
		elif backSide[3]=="w" and rightSide[5]==color:
			sol.extend(["D", "R", "D'"])
		elif backSide[5]=="w" and leftSide[3]==color:
			sol.extend(["D'", "L'", "D"])
		elif frontSide[5]=="w" and rightSide[3]==color:
			sol.extend(["D", "R'", "D'"])
		elif frontSide[3]=="w" and leftSide[5]==color:
			sol.extend(["D'", "L", "D"])
		elif backSide[5]==color and leftSide[3]=="w":
			sol.extend(["D", "D", "B", "D", "D"])
		elif backSide[3]==color and rightSide[5]=="w":
			sol.extend(["D", "D", "B'", "D", "D"])
		return sol

	def greenCubicle(self):
		w, y, g, b = self.wSide , self.ySide , self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		x = self.whiteY(w, y, g, b, o, r, "g")
		y = self.whiteW(w, g, b, o, r, "g")
		z = self.white(w, g, b, o, r, "g")
		for i in [x,y,z]:
			if i != []:
				self.solution.extend(i)
				self.move(i)

	def redCubicle(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotate(w)
		self.rotatePrime(y)
		x = self.whiteY(w, y, r, o, g, b, "r" )
		y = self.whiteW(w, r, o, g, b, "r" )
		z = self.white(w, r, o, g, b, "r" )
		for i in [x,y,z]:
			if i != []:
				translation = self.translateLeft(i)
				self.solution.extend(translation)
				self.move(translation)

	def orangeCubicle(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotatePrime(w)
		self.rotate(y)
		x = self.whiteY(w, y, o, r, b, g, "o")
		y = self.whiteW(w, o, r, b, g, "o")
		z = self.white(w, o, r, b, g, "o")
		for i in [x,y,z]:
			if i != []:
				translation = self.translateRight(i)
				self.solution.extend(translation)
				self.move(translation)

	def blueCubicle(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotate(w); self.rotate(w)
		self.rotate(y); self.rotate(y)
		x = self.whiteY(w, y, b, g, r, o, "b")
		y = self.whiteW(w, b, g, r, o, "b")
		z = self.white(w, b, g, r, o, "b")
		for i in [x,y,z]:
			if i != []:
				translation = self.translateBack(i)
				self.solution.extend(translation)
				self.move(translation)








cross = SolveCross( gSide,bSide,wSide, ySide,  rSide, oSide)
cross.move(["U'", "R", "R", "B", "B", "D", "L'", "B'", "U", "L", "R", "D'"])
cross.redCubicle()
cross.greenCubicle()
cross.orangeCubicle()
cross.blueCubicle()
print (cross.getSolution())
cross.printCube()
