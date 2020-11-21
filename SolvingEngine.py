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
	def whiteY(self):
		sol = []
		if wSide[1]=="w" and gSide[7]=="g":
			sol.extend([])
		elif ySide[7]=="w" and gSide[1]=="g":
			sol.extend(["F", "F"])
		elif ySide[7]=="g" and gSide[1]=="w":
			sol.extend(["U'", "R'", "F", "R"])
		elif ySide[5]=="w" and oSide[1]=="g":
			sol.extend(["U", "F", "F"])
		elif ySide[5] == "g" and oSide[1] == "w":
			sol.extend(["R'", "F", "R"])
		elif ySide[3]=="w" and rSide[1]=="g":
			sol.extend(["U'", "F", "F"])
		elif ySide[3]=="g" and rSide[1]=="w":
			sol.extend(["L", "F'", "L'"])
		elif ySide[1]=="w" and bSide[1]=="g":
			sol.extend(["U", "U", "F", "F"])
		elif ySide[1]=="g" and bSide[1]=="w":
			sol.extend(["U", "R'", "F", "R"])
		return sol
	# Same as above, just for the white side
	def whiteW(self):
		sol = []
		if wSide[1]=="w" and gSide[7]=="g":
			sol.extend([])
		elif wSide[3]=="w" and rSide[7]=="g":
			sol.extend(["L", "L", "U'", "F", "F"])
		elif wSide[5]=="w" and oSide[7]=="g":
			sol.extend(["R", "R", "U", "F", "F"])
		elif wSide[7]=="w" and bSide[7]=="g":
			sol.extend(["B", "B", "U", "U", "F", "F"])
		elif wSide[1]=="g" and gSide[7]=="w":
			sol.extend(["F'", "D", "R'", "D'"])
		elif wSide[3]=="g" and rSide[7]=="w":
			sol.extend(["L'", "F'"])
		elif wSide[5]=="g" and oSide[7]=="w":
			sol.extend(["R", "F"])
		elif wSide[7]=="g" and bSide[7]=="w":
			sol.extend(["B","R'","U", "R", "F", "F"])
		return sol
	# Same as above, but for rest of sides
	def white(self):
		sol = []
		if wSide[1] == "w" and gSide[7] == "g":
			sol.extend([])
		elif gSide[5]=="g" and oSide[3]=="w":
			sol.extend(["F"])
		elif   gSide[3]=="g" and rSide[5] =="w":
			sol.extend(["F'"])
		elif bSide[3]=="w" and oSide[5]=="g":
			sol.extend(["D", "R", "D'"])
		elif bSide[5]=="w" and rSide[3]=="g":
			sol.extend(["D'", "L'", "D"])
		elif gSide[5]=="w" and oSide[3]=="g":
			sol.extend(["D", "R'", "D'"])
		elif gSide[3]=="w" and rSide[5]=="g":
			sol.extend(["D'", "L", "D"])
		elif bSide[5]=="g" and rSide[3]=="w":
			sol.extend(["D", "D", "B", "D", "D"])
		elif bSide[3]=="g" and oSide[5]=="w":
			sol.extend(["D", "D", "B'", "D", "D"])
		return sol





cross = SolveCross( gSide,bSide,wSide, ySide,  rSide, oSide)
cross.move(["R", "F", "U", "L", "D"])
cross.greenWhitey()
cross.greenWhitew()
print (cross.getSolution())
cross.printCube()
