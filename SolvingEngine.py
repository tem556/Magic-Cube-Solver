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

# Helper functions, used for solving the cube
# Function that translates the instructions for solving cube
# in case the cube is rotated left, Used for reusing solve green
# white cross function for other sides as well (for red side)
def translateLeft(list):
	if list == []:
		return []
	if list[0]=="F": return ["L"] + translateLeft(list[1:])
	if list[0]=="F'": return ["L'"] + translateLeft(list[1:])
	if list[0]=="R": return ["F"] + translateLeft(list[1:])
	if list[0]=="R'": return ["F'"] + translateLeft(list[1:])
	if list[0]=="L": return ["B"] + translateLeft(list[1:])
	if list[0]=="L'": return ["B'"] + translateLeft(list[1:])
	if list[0]=="B": return  ["R"] + translateLeft(list[1:])
	if list[0]=="B'": return ["R'"] + translateLeft(list[1:])
	if list[0]=="D" or list[0]=="D'":
		return [list[0]] + translateLeft(list[1:])
	if list[0]=="U" or list[0]=="U'":
		return[list[0]] + translateLeft(list[1:])


# Same as above, only if rotated right (orange side)
def translateRight(list):
	if list == []:
		return []
	if list[0]=="F": return ["R"] + translateRight(list[1:])
	if list[0]=="F'": return ["R'"] + translateRight(list[1:])
	if list[0]=="R": return ["B"] + translateRight(list[1:])
	if list[0]=="R'": return ["B'"] + translateRight(list[1:])
	if list[0]=="L": return ["F"] + translateRight(list[1:])
	if list[0]=="L'": return ["F'"] + translateRight(list[1:])
	if list[0]=="B": return  ["L"] + translateRight(list[1:])
	if list[0]=="B'": return ["L'"] + translateRight(list[1:])
	if list[0] == "D" or list[0] == "D'":
		return [list[0]] + translateRight(list[1:])
	if list[0] == "U" or list[0] == "U'":
		return [list[0]] + translateRight(list[1:])

# Used if the cube is rotated 180 degrees, (blue side)
def translateBack(list):
	if list == []:
		return []
	if list[0]=="F": return ["B"] + translateBack(list[1:])
	if list[0]=="F'": return ["B'"] + translateBack(list[1:])
	if list[0]=="R": return ["L"] + translateBack(list[1:])
	if list[0]=="R'": return ["L'"] + translateBack(list[1:])
	if list[0]=="L": return ["R"] + translateBack(list[1:])
	if list[0]=="L'": return ["R'"] + translateBack(list[1:])
	if list[0]=="B": return  ["F"] + translateBack(list[1:])
	if list[0]=="B'": return ["F'"] + translateBack(list[1:])
	if list[0] == "D" or list[0] == "D'":
		return [list[0]] + translateBack(list[1:])
	if list[0] == "U" or list[0] == "U'":
		return [list[0]] + translateBack(list[1:])


# This class solves the cross for any cube permutation
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
		elif ySide[3]=="w" and leftSide[1]==color:
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
			sol.extend(["F'", "D", "R'", "D'"])
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


	#Uses the above function to put green cubicle in correct place
	#The function was written originally for green so requires minimal changes
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

	# Uses the solve cross functions, only difference is, the functions
	# were written assuming green as the front-side, makes use of that
	# by "rotating" the cube and making red the front side
	# That way, the logic for the green side still holds
	def redCubicle(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		# Rotates the white and yellow side as rotating the cube
		# mixes up the indices for those lists otherwise
		self.rotate(w)
		self.rotatePrime(y)
		# Gives red side as the front side for solving
		x = self.whiteY(w, y, r, o, g, b, "r" )
		y = self.whiteW(w, r, o, g, b, "r" )
		z = self.white(w, r, o, g, b, "r" )
		# After checking in all positions, executes the one
		# which holds the solution for current position
		for i in [x,y,z]:
			if i != []:
				# Translates the moves for a left rotated cube
				# into what it would look like with the green side as front
				translation = translateLeft(i)
				self.solution.extend(translation)
				self.move(translation)

	# Same logic as red side, only applied for orange side
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
				translation = translateRight(i)
				self.solution.extend(translation)
				self.move(translation)

	# Same logic as red side, only applied for blue side
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
				translation = translateBack(i)
				self.solution.extend(translation)
				self.move(translation)

	def solveAllSides(self):
		self.greenCubicle()
		self.redCubicle()
		self.orangeCubicle()
		self.blueCubicle()
		self.solution.extend(["Cross Solved"])


	def getSides(self):
		return (wSide, ySide, gSide, bSide, oSide, rSide)



cross = SolveCross( gSide,bSide,wSide, ySide,  rSide, oSide)
cross.move(['U', 'D',"R","F","U'","D","B"])
cross.solveAllSides()
# z = cross.getSides()


# Solves first two layers of the cube after having the cross done
# whiteSide, yellowSide, frontSide, backSide, rightSide, leftSide
class SolveFirstTwoLayers(RubikCube):

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


	def easyCases(self, w, y, f, b, r, l):
		# Saves the colors for the front side and the right side
		# Are the colors we are looking for.
		fC, rC = f[4], r[4]
		if f[2]==fC and r[0]=="w" and y[8]==rC and y[1]==fC and b[1]==rC:
			return ["R", "U", "R'"]
		elif f[2]=="w" and r[0]==rC and y[8]==fC and y[3]==rC and l[1]==fC:
			return ["F'", "U'", "F"]
		elif f[2]==fC and r[0]=="w" and y[8]==rC and y[7]==rC and f[1]==fC:
			return ["U'", "F'", "U", "F"]
		elif f[2]=="w" and r[0]==rC and y[8]==fC and y[5]==fC and r[1]==rC:
			return ["U", "R", "U'", "R'"]
		elif f[1]==fC and f[8]==fC and  r[6]==rC and w[2]=="w" and y[7]==rC:
			return ["U", "R", "U'", "R'", "U'", "F'", "U", "F"]
		elif r[1]==rC and f[8]==fC and r[6]==rC and w[2]=="w" and y[5]==fC:
			return ["U'", "F'", "U", "F", "U", "R", "U'", "R'"]
		elif f[1]==fC and y[7]==rC and f[8]==rC and r[6]=="w" and w[2]==fC:
			return ["F'", "U", "F", "U'", "F'", "U", "F"]
		elif r[1]==rC and y[5]==fC and f[8]==rC and r[6]=="w" and w[2]==fC:
			return ["R", "U", "R'", "U'", "R", "U", "R'"]

	def casesPartTwo(self, w, y, f, b, r, l):
		fC, rC = f[4], r[4]
		if f[8]=="w" and r[6]==fC and w[2]==rC and y[5]==fC and r[1]==rC:
			return ["R", "U'", "R'", "U", "R", "U'", "R'"]
		elif f[1]==fC and y[7]==rC and f[8]=="w" and r[6]==fC and w[2]==rC:
			return ["F'", "U'", "F", "U", "F'", "U'", "F"]
		elif f[5]==fC and r[3]==rC and y[8]=="w" and f[2]==rC and r[0]==fC:
			return ["R", "U", "R'", "U'", "R", "U", "R'", "U'", "R", "U", "R'"]
		elif f[5]==rC and r[3]==fC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["R", "U'", "R'", "U", "F'", "U", "F"]
		elif f[5]==fC and r[3]==rC and f[2]==fC and y[8]==rC and r[0]=="w":
			return ["U", "F'", "U", "F", "U", "F'", "U", "U", "F"]
		elif f[5]==rC and r[3]==fC and f[2]==fC and r[0]=="w" and y[8]==rC:
			return ["U", "F'", "U'", "F", "U'", "R", "U", "R'"]
		elif f[5]==fC and r[3]==rC and f[2]=="w" and r[0]==rC and y[8]==fC:
			return ["U'", "R", "U'", "R'", "U'", "R", "U", "U", "R'"]
		elif f[5]==rC and r[3]==fC and f[2]=="w" and y[8]==fC and r[0]==rC:
			return ["U'", "R", "U", "R'", "U", "F'", "U'", "F"]
		elif y[5]==rC and r[1]==fC and f[2]==fC and y[8]==rC and r[0]=="w":
			return ["R", "U'", "R'", "U", "U", "F'", "U'", "F"]

	def casesPartThree (self, w, y, f, b, r, l):
		fC, rC = f[4], r[4]
		if f[1]==rC and y[7]==fC and f[2]=="w" and r[0]==rC and y[8]==fC:
			return ["F'","U", "F", "U'", "U'", "R", "U", "R'"]
		elif y[1]==rC and b[1]==fC and f[2]==fC and y[8]==rC and r[0]=="w":
			return ["U", "F'", "U", "U", "F", "U", "F'", "U", "U", "F"]
		elif f[2]=="w" and r[0]==rC and y[8]==fC and y[3]==fC and l[1]==rC:
			return ["U'", "R", "U", "U", "R'", "U'", "R", "U", "U", "R'"]
		elif y[3]==rC and l[1]==fC and f[2]==fC and y[8]==rC and r[0]=="w":
			return ["U", "F'", "U'", "F", "U", "F'", "U", "U", "F"]
		elif y[1]==fC and b[1]==rC and f[2]=="w" and r[0]==rC and y[8]==fC:
			return ["U'", "R", "U", "R'", "U'", "R", "U", "U", "R'"]
		elif r[1]==rC and y[5]==fC and f[2]==fC and r[0]=="w" and y[8]==rC:
			return ["U'", "R", "U'", "R'", "U", "R", "U", "R'"]
		elif f[1]==fC and y[7]==rC and r[0]==rC and y[8]==fC and f[2]=="w":
			return ["U", "F'", "U", "F", "U'", "F'", "U'", "F"]
		elif y[3]==fC and l[1]==rC and f[2]==fC and y[8]==rC and r[0]=="w":
			return ["U'", "R", "U", "R'", "U", "R", "U", "R'"]
		elif y[1]==rC and b[1]==fC and f[2]=="w" and y[8]==fC and r[0]==rC:
			return ["U", "F'", "U'", "F", "U'", "F'", "U'", "F"]

	def casesPartFour (self, w, y, f, b, r, l):
		fC, rC = f[4], r[4]
		if f[1]==rC and y[7]==fC and f[2]==fC and y[8]==rC and r[0]=="w":###
			return  ["U", "F'", "U", "U", "F", "U'", "R", "U", "R'"]
		elif r[1]==fC and y[5]==rC and f[2]=="w" and y[8]==fC and r[0]==rC:
			return ["U'", "R", "U", "U", "R'", "U", "F'", "U'", "F"]
		elif f[1]==rC and y[7]==fC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["R", "U", "R'", "U'", "U'", "R", "U", "R'", "U'", "R", "U", "R'"]
		elif r[1]==fC and y[5]==rC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["F'", "U'", 'F', 'U', 'U', "F'", "U'", 'F', 'U', "F'", "U'", 'F']
		elif y[3]==fC and l[1]==rC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["U", "U", "R", "U", "R'", "U", "R", "U'", "R'"]
		elif y[1]==rC and b[1]==fC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["U", "U", "F'", "U'", "F", "U'", "F'", "U", "F"]
		elif y[1]==fC and b[1]==rC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["U", "R", "U", "U", "R'", "U", "R", "U'", "R'"]
		elif y[3]==rC and l[1]==fC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["U'", "F'", "U", "U", "F", "U'", "F'", "U", "F"]
		elif r[1]==rC and y[5]==fC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["R", "U", "U", "R'", "U'", "R", "U", "R'"]

	def casesPartFive (self, w, y, f, b, r, l):
		fC, rC = f[4], r[4]
		if f[1]==fC and y[7]==rC and f[2]==rC and r[0]==fC and y[8]=="w":
			return ["F'", "U", "U", "F", "U", "F'", "U'", "F"]
		elif f[5]==rC and r[3]==fC and f[8]==fC and r[6]==rC and w[2]=="w":
			return ["R", "U'", "R'", "U", "F'", 'U', 'U', 'F', 'U', "F'", 'U', 'U','F']
		elif f[5]==fC and r[3]==rC and f[8]==rC and r[6]=="w" and w[2]==fC:
			return ["R", "U'", "R'", "U", "R", "U", "U", "R'", "U", "R", "U'", "R'"]
		elif f[5]==fC and r[3]==rC and f[8]=="w" and r[6]==fC and w[2]==rC:
			return ["R", "U'", "R'", "U'", "R", "U", "R'", "U'", "R", "U", "U", "R'"]
		elif f[5]==rC and r[3]==fC and f[8]==rC and r[6]=="w" and w[2]==fC :
			return ["R", "U", "R'", "U'", "R", "U'", "R'", "U", "U", "F'", "U'", "F"]
		elif f[5]==rC and r[3]==fC and f[8]=="w" and r[6]==fC and w[2]==rC:
			return ["R", "U'", "R'", "U", "F'", "U'", "F", "U'", "F'", "U'", "F"]

	def greenFirstTwoLayers(self):
		w, y, g, b = self.wSide, self.ySide, self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		final1 = self.easyCases(w, y, g, b, o, r)
		final2 = self.casesPartTwo(w, y, g, b, o, r)
		final3 = self.casesPartThree(w, y, g, b, o, r)
		final4 = self.casesPartFour(w, y, g, b, o, r)
		final5  = self.casesPartFive(w, y, g, b, o, r)
		for i in [final1, final2, final3, final4, final5]:
			if i!=None and i!=[]:
				return i

	def orangeFirstTwoLayers(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotatePrime(w)
		self.rotate(y)
		final1 = self.easyCases(w, y, o, r, b, g)
		final2 = self.casesPartTwo(w, y, o, r, b, g)
		final3 = self.casesPartThree(w, y, o, r, b, g)
		final4 = self.casesPartFour(w, y, o, r, b, g)
		final5 = self.casesPartFive(w, y, o, r, b, g)
		for i in [final1, final2, final3, final4, final5]:
			if i != None and i != []:
				translation = translateRight(i)
				return translation

	def redFirstTwoLayers(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotate(w)
		self.rotatePrime(y)
		final1 = self.easyCases(w, y, r, o, g, b)
		final2 = self.casesPartTwo(w, y, r, o, g, b)
		final3 = self.casesPartThree(w, y, r, o, g, b)
		final4 = self.casesPartFour(w, y, r, o, g, b)
		final5 = self.casesPartFive(w, y, r, o, g, b)
		for i in [final1, final2, final3, final4, final5]:
			if i != None and i != []:
				translation = translateLeft(i)
				return translation

	def blueFirstTwoLayers(self):
		w, y, g, b = self.wSide[:], self.ySide[:], self.gSide, self.bSide
		r, o = self.rSide, self.oSide
		self.rotate(w);self.rotate(w)
		self.rotate(y);self.rotate(y)
		final1 = self.easyCases(w, y, b, g , r, o)
		final2 = self.casesPartTwo(w, y, b, g, r, o)
		final3 = self.casesPartThree(w, y, b, g, r, o)
		final4 = self.casesPartFour(w, y, b, g, r, o)
		final5 = self.casesPartFive(w, y, b, g, r, o)
		for i in [final1, final2, final3, final4, final5]:
			if i != None and i != []:
				translation = translateBack(i)
				return translation

	# Function used for trying out different orders of solving
	def tryRotate(self, func):
		x = func()
		if x==None:
			self.move(["U"]);self.solution.extend(["U"])
			x = func()
		if x==None:
			self.move(["U"]);self.solution.extend(["U"])
			x = func()
		if x==None:
			self.move(["U", "U"]); self.solution = self.solution[:-2]
			self.move(["U'"]); self.solution.extend(["U'"])
			x = func()
		if x!=None:
			self.move(x);self.solution.extend(x)
			return False
		else:
			self.move(["U"]);self.solution = self.solution[:-1]
			return True

	def greenContinued(self):
		condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			move = ["F", "U", "F'"]
			self.move(move)
			self.solution.extend(move)
			condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			move = ["R'", "U", "R"]
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			self.move(["R'", "U'","U'", "R"])
			self.solution = self.solution[:-6]
			move = ["L", "U'", "L'"]
			self.move(move);self.solution.extend(move)
			condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.greenFirstTwoLayers)
		if condition :
			# Cancels the changes made from previous attempt
			self.move(["L", "U", "L'"])
			self.solution = self.solution[:-3]
			self.move(["U", "U", "R'", "U", "R"])
			self.solution.extend(["U", "U", "R'", "U", "R"])
			condition = self.tryRotate(self.greenFirstTwoLayers)


	def orangeContinued (self):
		condition = self.tryRotate(self.orangeFirstTwoLayers)
		if condition :
			move = ["B'", 'U', 'B']
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.orangeFirstTwoLayers)
		if condition :
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.orangeFirstTwoLayers)
		if condition :
			self.move(["B'", "U'", "U'", 'B'])
			self.solution = self.solution[:-6]
			move = ['F', "U'", "F'"]
			self.move(move);self.solution.extend(move)
			condition = self.tryRotate(self.orangeFirstTwoLayers)
		if condition :
			self.move(move); self.solution.extend(move)
			condition = self.tryRotate(self.orangeFirstTwoLayers)
		if condition :
			# Cancels the changes made from previous attempt
			self.move(['F', "U'", "F'"])
			self.solution = self.solution[:-3]
			self.move(['U', 'U', "B'", 'U', 'B'])
			self.solution.extend(['U', 'U', "B'", 'U', 'B'])
			condition = self.tryRotate(self.orangeFirstTwoLayers)

	def blueContinued (self):
		condition = self.tryRotate(self.blueFirstTwoLayers)
		if condition:
			move = ["L'", 'U', 'L']
			self.move(move)
			self.solution.extend(move)
			condition = self.tryRotate(self.blueFirstTwoLayers)
		if condition:
			self.move(move)
			self.solution.extend(move)
			condition = self.tryRotate(self.blueFirstTwoLayers)

	def redContinued(self):
		condition = self.tryRotate(self.redFirstTwoLayers)
	def solveTwoLayers(self):
		self.greenContinued()
		self.solution.extend(["green done"])
		self.orangeContinued()
		self.solution.extend(["orange done"])
		self.blueContinued()
		self.solution.extend(["blue done"])
		self.redContinued()
		self.solution.extend(["red done"])

	def getSides(self):
		return (wSide, ySide, gSide, bSide, oSide, rSide)



w, y, g, b, o, r = cross.getSides()
#
crossSolution = cross.getSolution()
layer = SolveFirstTwoLayers(g, b, w, y, r, o, crossSolution )
layer.solveTwoLayers()
layerSolution = layer.getSolution()
# layer.printCube()


# Solves the final part of the cube
class LastLayer(RubikCube):
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

		for i in range(1, len(sol)):
			if sol[i]==sol[i-1]:
				sol[i], sol[i-1] =  "X", sol[i]+"2"
		# "Deleted" moves were converted into X's before, now will be deleted
		while "X" in sol:
			sol.remove("X")
		while "X2" in sol:
			sol.remove("X2")
		return sol

	def yellowCross(self):
		y = self.ySide
		if y[1]!="y" and y[3]!="y" and y[5]!="y" and y[7]!="y":
			self.solution.extend(["F", "R", "U", "R'", "U'", "F'"])
			self.move(["F", "R", "U", "R'", "U'", "F'"])
		if y[5]=="y" and y[7]=="y" and y[1]!="y" and y[3]!="y":
			self.solution.extend(["B", "U", "L", "U'", "L'", "B'"])
			self.move(["B", "U", "L", "U'", "L'", "B'"])
		elif y[1]=="y" and y[3]=="y" and y[5]!="y" and y[7]!="y":
			self.solution.extend(["U", "U", "B", "U", "L", "U'", "L'", "B'"])
			self.move(["U", "U", "B", "U", "L", "U'", "L'", "B'"])
		elif y[1]=="y" and y[5]=="y" and y[3]!="y" and y[7]!="y":
			self.solution.extend(["U", "B", "U", "L", "U'", "L'", "B'"])
			self.move(["U", "B", "U", "L", "U'", "L'", "B'"])
		elif y[3]=="y" and y[7]=="y" and y[1]!="y" and y[5]!="y":
			self.solution.extend(["U'", "B", "U", "L", "U'", "L'", "B'"])
			self.move(["U'", "B", "U", "L", "U'", "L'", "B'"])
		elif y[1]=="y" and y[7]=="y" and y[5]!="y" and y[3]!="y":
			self.solution.extend(["U", "F", "R", "U", "R'", "U'", "F'" ])
			self.move(["U", "F", "R", "U", "R'", "U'", "F'" ])
		elif y[3]=="y" and y[5]=="y" and y[1]!="y" and y[7]!="y":
			self.solution.extend(["F", "R", "U", "R'", "U'", "F'"])
			self.move(["F", "R", "U", "R'", "U'", "F'"])

	def allYellow(self):
		y,f,r,l = self.ySide, self.gSide, self.oSide, self.rSide
		if y[2]=="y" and y[0]!="y" and y[6]!="y" and y[8]!="y" and r[0]=="y":
			return ["R", "U", "U", "R'", "U'", "R", "U'", "R'"]
		elif y[0]!="y" and y[2]!="y" and y[6]=="y" and y[8]!="y" and f[2]=="y":
			return ["R", "U", "R'", "U", "R", "U", "U", "R'"]
		elif y[0]!="y" and y[2]=="y" and y[6]!="y" and y[8]=="y" and f[0]=="y":
			return ["L", "F", "R'", "F'", "L'", "F", "R", "F'"]
		elif y[0]!="y" and y[2]=="y" and y[6]=="y" and y[8]=="y" and f[2]=="y":
			return ["F'", "L", "F", "R'", "F'", "L'", "F", "R"]
		elif y[0]=="y" and y[2]=="y" and y[6]!="y" and y[8]!="y" and f[0]=="y":
			return ["R", "R", "D", "R'", "U", "U", "R", "D'", "R'", "U", "U", "R'"]
		elif y[0]!="y" and y[2]!="y" and y[6]!="y" and y[8]!="y" and f[2]=="y" and l[0]=="y":
			return ["R","U","U","R","R","U'","R","R","U'","R","R","U","U", "R'"]
		elif y[0]!="y" and y[2]!="y" and y[6]!="y" and y[8]!="y" and r[2]=="y" and l[2]=="y":
			return ["R", "U", "R'", "U", "R", "U'", "R'", "U", "R", "U", "U" , "R'"]

	def tryRotate(self, func):
		x = func()
		if x==None:
			self.move(["U"]);self.solution.extend(["U"])
			x = func()
		if x==None:
			self.move(["U"]);self.solution.extend(["U"])
			x = func()
		if x==None:
			self.move(["U", "U"]); self.solution = self.solution[:-2]
			self.move(["U'"]); self.solution.extend(["U'"])
			x = func()
		if x!=None:
			self.move(x);self.solution.extend(x)
			return False
		else:
			self.move(["U"]);self.solution = self.solution[:-1]
			return True

	# Has the cases with a probability of 1/18
	def pLLPartOne(self):
		y, f, r, l = self.ySide, self.gSide, self.oSide, self.rSide
		b = self.bSide
		if b[0]==b[1] and b[1]==b[2] and f[1]==r[0] and r[0]==r[2]:
			return ["R", "R", "U", "R", "U", "R'","U'", "R'", "U'", "R'", "U", "R'"]
		elif b[0]==b[1] and b[1]==b[2] and f[1]==l[0] and l[0]==l[2]:
			return ["R","U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R", "R"]
		elif f[0]==f[1] and l[1]==l[2] and b[0]==b[2] and b[1]==l[0]:
			return ["R'", "F", "R'", "B", "B", "R", "F'", "R'", "B", "B", "R", "R"]
		elif f[0]==f[1] and l[1]==l[2] and r[0]==r[2] and r[1]==l[0]:
			return ["R", "R", "B", "B", "R", "F", "R'", "B", "B", "R", "F'", "R"]
		elif l[0]==l[2] and f[0]==f[1] and l[1]==b[2] and b[0]==f[2]:
			return ['B','U','U',"B'",'U','U','B',"L'","B'","U'",'B','U','B','L','B','B','U']
		elif l[1]==l[2] and f[0]==f[2] and l[0]==r[2] and [1]==f[0]:
			return ["R'","U","U","R'","D'","R","U'","R'","D","R","U","R","U'","R'","U'","R","U'"]
		elif f[0]==f[1] and f[1]==f[2] and r[0]==r[1] and l[2]==b[1]:
			return ["R'","U","L'","U","U","R","U'","R'","U","U","R","L","U'"]
		elif l[0]==l[1] and l[1]==l[2] and b[1]==b[2] and f[0]==r[1]:
			return ["R","U","R'","F'","R","U","R'","U'","R'","F","R","R","U'","R'","U'"]
		elif f[0]==f[1] and b[1]==b[2] and l[0]==l[2] and r[1]==l[0]:
			return ["R","U","R'","U'","R'","F","R","R","U'","R'","U'","R","U","R'","F'"]
		elif l[0]==l[1] and l[1]==l[2] and r[0]==b[2] and r[2]==f[0]:
			return ["R'","U'","F'","R","U","R'","U'","R'","F","R","R","U'","R'","U'","R","U","R'","U","R"]

	def pLLPartTwo(self):
		y, f, r, l = self.ySide, self.gSide, self.oSide, self.rSide
		b = self.bSide
		if l[1]==l[2] and f[0]==f[1] and r[0]==l[1] and r[1]==b[0]:
			return ["R'","U","R'","U'","B'","R'",'B','B',"U'","B'",'U',"B'",'R','B','R']
		elif f[0]==f[1] and r[1]==r[2] and f[2]==l[1] and r[0]==l[2]:
			return ["F","R","U'","R'","U'","R","U","R'","F'","R","U","R'","U'","R'","F","R","F'"]
		elif l[0]==[2] and f[1]==f[2] and f[0]==b[1] and l[2]==r[1]:
			return ["R","R","U","R'","U","R'","U'","R","U'","R","R","D","U'","R'","U","R","D'","U"]
		elif f[1]==f[2] and b[0]==b[2] and r[1]==b[0] and f[0]==l[1]:
			return ["F'","U'","F","R","R","D","B'",'U','B',"U'",'B',"D'","R","R"]
		elif l[0]==l[2] and b[0]==b[1] and f[1]==b[1] and l[1]==r[2]:
			return ["R", "R", "U'", "R","U'","R","U","R'","U","R","R","D'","U","R","U'","R'","D","U'"]
		elif l[0]==l[2] and r[0]==r[1] and f[1]==l[0] and f[0]==b[1]:
			return ["R", "U","R'","F","F","D'",'L', "U'", "L'", 'U', "L'", "D", "F","F"]

	def pLLPartThree(self):
		y, f, r, l = self.ySide, self.gSide, self.oSide, self.rSide
		b = self.bSide
		if f[1]==b[0] and b[0]==b[2] and r[1]==l[0] and l[0]==l[2]:
			return ["L'", "R'", "U","U","L","R","F","B","U","U","F'","B'"]
		elif  f[1]==r[0] and r[0]==r[2] and l[1]==b[0] and b[0]==b[2]:
			return ["R","B'","R'","B","F","R'","F","B'","R'","B","R","F","F"]
		elif r[0]==l[2] and r[2]==l[0] and f[0]==b[2] and f[2]==b[0]:
			return ["F","R","B","R'","F'","R","L","F","L'","B'","L","F'","R'","L'"]
		elif f[0] == f[1] and l[0] == l[1] and f[2] == b[1] and l[2] == r[1]:
			return ["R","U'","R","R","F","F","U'","R","F","F","R'","U","F","F","R","R","U","R'"]
		elif f[1] == f[2] and l[2] == l[1] and f[0] == b[1] and r[0] == l[1]:
			return ["R'", "U", "R","R","B","B","U","R'","B","B","R","U'","B","B","R","R","U'","R"]

	def finishCube(self):
		self.yellowCross()
		self.tryRotate(self.allYellow)
		self.tryRotate(self.pLLPartOne)
		self.tryRotate(self.pLLPartTwo)
		self.tryRotate(self.pLLPartThree)
		if self.gSide[1]=="r":
			self.solution.extend(["U"])
			self.move(["U"])
		elif self.gSide[1]=="b":
			self.solution.extend(["U","U"])
			self.move(["U", "U"])
		elif self.gSide[1]=="o":
			self.solution.extend(["U'"])
			self.move(["U'"])




w, y, g, b, o, r = layer.getSides()
yellow = LastLayer(g, b, w, y, r, o, layerSolution)
yellow.finishCube()
yellow.printCube()
print (yellow.getSolution())













