
from lib.loginDetails import loginDetails
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
from Event import Event
class schoolDetails(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.master = master
		self.grid()
		self.logo()
		self.loginInput()
		self.master.bind("<Return>", self.enterLogin)

	def __str__(self):
		return str(self.schoolName.get())


		
	def logo(self):
		# Adds the university logo to the top left corner
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row = 1, column = 1, columnspan = 2)

	def loginInput(self):

		lblSchool = Label(self, text = 'What School are you from?: ')
		lblSchool.grid(row = 2, column = 1)



		schoolNames = Event.getSchools()
		self.schoolName = StringVar()
		self.schoolName.set(schoolNames[0])

		self.optSchool = OptionMenu(self, self.schoolName, *schoolNames)
		self.optSchool["width"] =10
		self.optSchool.grid(row = 3, column = 1,sticky =EW)

		self.btnSubmit = Button(self, text = 'Enter School Details', command = self.validateLogin)
		self.btnSubmit.grid(row = 4, column = 1, columnspan = 2)

		btnCancel = Button(self, text = 'Cancel', command = self.cancelLogin)
		btnCancel.grid(row = 5, column = 1, columnspan = 2)

	def enterLogin(self,event):
		self.validateLogin()

	def cancelLogin(self):
		self.master.destroy()

	def validateLogin(self):
		# store school details here

		self.master.master.destroy()
		import mainQuizWindow
		mainQuizWindow.main(self.schoolName.get())


			
