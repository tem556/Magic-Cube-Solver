import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from ImageProcessing import *
from RubiksCube import *
from SolvingEngine import *

class GUI:
	def __init__(self, window):
		# Has the font used in the windows
		self.textFont= font.Font(size =20, weight="bold")
		self.textFont2= font.Font(size =25, weight="bold")
		self.textFont3 = font.Font(size=15)
		self.window = window
		self.imgProc = GetColors()
		self.captureCondition = True
		self.gSide= []
		self.solutionIndex = -1
	# Creates the top portion of the window
	def topScreen(self):
		root = self.window
		textFont2=self.textFont2
		textFont=self.textFont
		# Makes a frame and puts a canvas in it along with a button
		topFrame = tk.Frame(root, width=640, height=320)
		firstBox = tk.Canvas(topFrame, width=640, height=230)

		buttonText1="Click here to capture the cube"
		captureButton = tk.Button(topFrame, height=1, width=25, text=buttonText1, font=textFont)
		captureButton["command"] = self.imgProcessing
		firstBox.create_rectangle((0,0), (320 ,320), fill="red")
		firstBox.create_rectangle((320, 0), (640, 320), fill="green")
		firstBox.create_text(320, 45, text="Welcome to Magic Cube Solver", fill="white", font=textFont2)

		firstBox.grid(row=0, column=0)
		captureButton.place(relx =0.157, rely= 0.4)
		topFrame.grid(row=0, column=0)


	# Uses the Solving Engine to get the solution
	def getSolution(self):
		gSide, oSide, bSide = self.gSide, self.oSide, self.bSide
		rSide, wSide, ySide = self.rSide, self.wSide, self.ySide
		cross = SolveCross(gSide, bSide, wSide, ySide, rSide, oSide, [])
		cross.solveAllSides()
		w, y, g, b, o, r = cross.getSides()
		crossSolution = cross.getSolution()
		layer = SolveFirstTwoLayers(g, b, w, y, r, o, [])
		layer.solveTwoLayers()
		layerSolution = layer.getSolution()
		w, y, g, b, o, r = layer.getSides()
		yellow = LastLayer(g, b, w, y, r, o, [])
		yellow.finishLastLayer()
		self.solution  = crossSolution+layerSolution+yellow.getSolution()
		print (self.solution)


	# Gets the colors and the solution for the cube
	def imgProcessing(self):
		message = "Are you sure you want to capture again?"
		if self.captureCondition:
			self.imgProc.finalStep()
			cSides = self.imgProc.getColor()
			self.gSide, self.bSide, self.wSide = cSides[0][:], cSides[1][:], cSides[2][:]
			self.ySide, self.rSide, self.oSide = cSides[3][:], cSides[4][:], cSides[5][:]
			gSide, oSide, bSide = self.gSide[:], self.oSide[:], self.bSide[:]
			rSide, wSide, ySide = self.rSide[:], self.wSide[:], self.ySide[:]
			self.unsolvedCube = RubikCube(gSide, bSide, wSide, ySide, rSide, oSide)
			self.getSolution()
			self.captureCondition = False
		elif messagebox.askyesno("Verify", message):
			self.captureCondition=True
			self.solution=[]
			self.solutionIndex=-1
			self.imgProcessing()

	def getInstructions(self):
		inst = "Step 1: Click on the first button to capture your"
		inst+= " Rubik's Cube's color.\nStep 2: Have the side with"
		inst+=" the 'Faces the Camera' color as centre piece facing the"
		inst+=" camera.\nAnd the side with the 'Faces Upwards' color as"
		inst+=" centre piece facing upwards.\nStep 3: Repeat the process"
		inst+=" for all six sides.\nStep 4: Click on the second button"
		inst+=" to get the solution.\nWarning: Inconsistent lighting"
		inst+=" conditions for capturing may result in inaccurate results."
		root=self.window
		window=tk.Toplevel(root)
		instructionCanvas = tk.Canvas(window, height=230, width=800)
		instructionCanvas.create_text(300, 20, text="Instructions:", font=self.textFont2)
		instructionCanvas.create_text(400, 130, text=inst, font=self.textFont3)
		instructionCanvas.pack()

	# Creates the bottom portion of the window
	# Also creates the instuctions button in the main window(root)
	def bottomScreen(self):
		root = self.window
		textFont = self.textFont
		# Makes a frame and puts a canvas in it along with a button
		bottomFrame = tk.Frame(root, width=640, height=320)

		secondBox = tk.Canvas(bottomFrame, width=640, height=230)
		secondBox.create_rectangle((0,0), (320 ,320), fill="blue")
		secondBox.create_rectangle((320, 0), (640, 320), fill="orange")
		buttonText2 = "Click here to get the solution"
		solutionButton = tk.Button(root, height=1, width=25, text=buttonText2, font=textFont)
		solutionButton["command"] = self.solutionScreen
		# Creates the window for the instructions
		buttonText3 = "Read the instructions here first"
		instructionButton = tk.Button(bottomFrame, height=1, width=25, text=buttonText3, font=textFont)
		instructionButton["command"]=self.getInstructions
		secondBox.grid(column=0, row=0)
		bottomFrame.grid(row=1, column=0)
		solutionButton.grid(row=0, column=0, rowspan=2)
		instructionButton.grid(row=0, column =0)
	# Converts the "g"s and etc. to "green" etc for color
	def makeColor(self, list):
		answer = []
		for i in list:
			if i=="g":
				answer.append("green")
			elif i=="b":
				answer.append("blue")
			elif i=="r":
				answer.append("red")
			elif i=="o":
				answer.append("orange")
			elif i=="w":
				answer.append("white")
			elif i=="y":
				answer.append("yellow")
		return answer
	# Makes a single side with nine blocks that follow the color provided in a list
	def createSide(self, sCrd, colorList):
		colorList = self.makeColor(colorList)
		sCrdX, sCrdY = sCrd
		self.cube2D.create_rectangle((sCrdX, sCrdY),(sCrdX+60, sCrdY+60) ,fill=colorList[0])
		self.cube2D.create_rectangle((sCrdX+60, sCrdY),(sCrdX+120, sCrdY+60), fill=colorList[1])
		self.cube2D.create_rectangle((sCrdX+120, sCrdY), (sCrdX+180, sCrdY+60), fill=colorList[2])
		self.cube2D.create_rectangle((sCrdX, sCrdY+60), (sCrdX+60, sCrdY+120), fill=colorList[3])
		self.cube2D.create_rectangle((sCrdX+60, sCrdY+60),(sCrdX+120, sCrdY+120), fill=colorList[4])
		self.cube2D.create_rectangle((sCrdX+120, sCrdY+60),(sCrdX+180, sCrdY+120), fill=colorList[5])
		self.cube2D.create_rectangle((sCrdX, sCrdY+120), (sCrdX+60, sCrdY+180),fill=colorList[6])
		self.cube2D.create_rectangle((sCrdX+60, sCrdY+120), (sCrdX+120, sCrdY+180), fill=colorList[7])
		self.cube2D.create_rectangle((sCrdX+120, sCrdY+120), (sCrdX+180, sCrdY+180), fill=colorList[8])
		text = "Please position the cube such that the green side"
		text+=" is facing you and the yellow side is facing upwards"
		self.cube2D.create_text(450,20, text=text, font=self.textFont3 )


	# Is executed when the solution button is pressed
	# Used the above function to show all side of the cube on canvas
	def solutionScreen(self):
		if self.gSide==[]:
			messagebox.showwarning("Warning","You have not captured the colors yet")
		else:
			root = self.window
			solutionWindow = tk.Toplevel(root, height=700, width=1000)
			self.cube2D = tk.Canvas(solutionWindow, height=650, width=1000)
			self.createSide((300,60), self.imgProc.ySide)
			self.createSide((300,250), self.imgProc.gSide)
			self.createSide((300,440), self.imgProc.wSide)
			self.createSide((110,250), self.imgProc.rSide)
			self.createSide((490,250), self.imgProc.oSide)
			self.createSide((680,250), self.imgProc.bSide)
			self.cube2D.pack()
			button = tk.Button(solutionWindow,text="Next Step", height=2)
			button["command"]=self.nextStep
			self.text = tk.Text(solutionWindow, height=2, width=10)
			self.text.insert("end", "Start")
			self.text.config(state="disabled")
			self.text.place(relx=0.5, rely=0.93)
			button.place(relx=0.7, rely=0.93)

	def nextStep(self):
		if self.solutionIndex!=len(self.solution)-1:
			self.solutionIndex+=1
			self.unsolvedCube.move([self.solution[self.solutionIndex]])
			gSide, bSide = self.unsolvedCube.gSide, self.unsolvedCube.bSide
			oSide, rSide = self.unsolvedCube.oSide, self.unsolvedCube.rSide
			wSide, ySide = self.unsolvedCube.wSide, self.unsolvedCube.ySide
			self.cube2D.delete("all")
			self.createSide((300, 60), ySide)
			self.createSide((300, 250), gSide)
			self.createSide((300, 440), wSide)
			self.createSide((110, 250), rSide)
			self.createSide((490, 250), oSide)
			self.createSide((680, 250), bSide)
			self.text.config(state="normal")
			self.text.delete(1.0,"end")
			self.text.insert("end", self.solution[self.solutionIndex])
			self.text.config(state="disabled")
		else:
			messagebox.showinfo("Finished", "You have finished solving the cube")
			# Resets the values after the cube has been solved once
			self.solution = []
			self.solutionIndex = -1






root = tk.Tk()
rubikscube = GUI(root)
rubikscube.topScreen()
rubikscube.bottomScreen()
root.mainloop()