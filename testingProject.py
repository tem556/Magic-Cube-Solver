import tkinter as tk

root = tk.Tk()
newWindow = tk.Toplevel(root)
newWindow.title("Solution")
cube2D = tk.Canvas(newWindow, height = 700, width = 1000)
cube2D.create_rectangle((300,50),(480,230) ,fill="yellow")
cube2D.create_rectangle((300,240),(480,420) ,fill="green")
cube2D.create_rectangle((300,430),(480,610) ,fill="white")

cube2D.create_rectangle((110,240),(290,420) ,fill="red")
cube2D.create_rectangle((490,240),(670,420) ,fill="orange")
cube2D.create_rectangle((680,240),(860,420) ,fill="blue")

# def createSide(startCrd, endCrd, colorList):







cube2D.pack()
root.mainloop()