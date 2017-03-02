from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
from Question import Question
import shelve
import shutil
import os

class addQuestion(Frame):
	# GUI Setup 

	def __init__(self, master):
		# initialise addQuestion class

		Frame.__init__(self, master)
		self.grid()


	def logo(self):
		# Adds the university logo to the top left corner
		logoCanvas = Canvas(self, width=150, height=149)
		logoCanvas.grid(row=1, column=1, rowspan=2, sticky=NE)

		self.logo = PhotoImage(file="Images/logo.gif")
		self.logo = self.logo.zoom(15)
		self.logo = self.logo.subsample(70)
		logoCanvas.create_image(75,75,image=self.logo)

	def logOut(self):

		btnLogOut = Button(text='Log Out',font=('Helvetica',16))
		btnLogOut.grid(row=1,column=3)


# Main
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

root.title("View/Edit Questions")
root.configure(background="gray80")
addQ = addQuestion(root)
root.mainloop()