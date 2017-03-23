
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
from Question import Question
import shelve
import shutil
import os

class addQuestToCat(Frame):
	# GUI Setup 


	def __init__(self, master, selCat = ""):
		# initialise addQuestion class
		self.selectedCat = selCat

		Frame.__init__(self, master)
		self.grid()
		self.logo()
		self.header()
		self.adminBtn()
		self.availableQuestions()
		self.submitButton()
		self.leavePage()
		self.questionsInCat()
		self.moveBtns()


	def logo(self):
        ## create logo
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row=0, column=0, rowspan =2 )

	def header(self):
		# Category Name and Window title
		lblHeader = Label(self, text='Add Questions', font=('Helvetica',32))
		lblHeader.grid(row=1, column=1, columnspan=2, sticky=NW)

		lblCatHeader = Label(self, text=self.selectedCat, font=('Helvetica',16))
		lblCatHeader.grid(row=0, column=1, columnspan=2, sticky=SW)

	def adminBtn(self):
		# Admin Options
		adminButton = Button(self, text='Admin Options',font=('Helvetica',16))
		adminButton["comman"] = self.master.destroy
		adminButton.grid(row=0, column=8, columnspan=1, sticky=E)

	def availableQuestions(self):

		lblLeft = Label(self, text='(Currently Available Questions)',font=('Helvetica',8,'bold'))
		lblLeft.grid(row=4, column=1, columnspan=2)

		self.listLeft = Listbox(self, height=20, selectmode = EXTENDED)
		scroll = Scrollbar(self, command=self.listLeft.yview)
		self.listLeft.configure(yscrollcommand=scroll.set)

		self.listLeft.grid(row=5, column=1, columnspan=3, rowspan=4)
		scroll.grid(row=5,column=4,rowspan=4,sticky=W)


		with shelve.open('questiondb') as db:
			for questionID in db.keys():
				if self.selectedCat not in db[questionID].category:
					questionText = db[questionID].entQuestion
					self.listLeft.insert(END,questionText)
		
		self.listLeft.config(width=40)


	def questionsInCat(self):
		lblRight = Label(self, text='(Questions currently in Category)',font=('Helvetica',8,'bold'))
		lblRight.grid(row=4, column=6, columnspan=2)

		self.listRight = Listbox(self, height=20, selectmode = EXTENDED)
		scroll = Scrollbar(self, command=self.listRight.yview)
		self.listRight.configure(yscrollcommand=scroll.set)

		self.listRight.grid(row=5, column=6, columnspan=3, rowspan =4)
		scroll.grid(row=5,column=9,rowspan=4,sticky=W)

		#this should pull questions from shelve file
		with shelve.open('questiondb') as db:
			for questionID in db.keys():
				if self.selectedCat in db[questionID].category:
					questionText = db[questionID].entQuestion
					self.listRight.insert(END,questionText)

		self.listRight.config(width=40)

	def moveQsRight(self):
		listOfSelected = self.listLeft.curselection()


		for i in range(len(listOfSelected)-1,-1,-1):

			self.listRight.insert(END, self.listLeft.get(listOfSelected[i]))
			self.listLeft.delete(listOfSelected[i])

	def moveQsLeft(self):
		listOfSelected = self.listRight.curselection()


		for i in range(len(listOfSelected)-1,-1,-1):

			self.listLeft.insert(END, self.listRight.get(listOfSelected[i]))
			self.listRight.delete(listOfSelected[i])

	def moveBtns(self):

		btnRight = Button(self, text=">")
		btnRight["command"] = self.moveQsRight
		btnRight.grid(row = 6, column =5)

		btnLeft = Button(self, text="<")
		btnLeft["command"] = self.moveQsLeft
		btnLeft.grid( row = 7, column = 5)

	def saveAndQuit(self):
		listOfSelected = len(self.listRight.get(0,END))

		listOfNotSelected = len(self.listLeft.get(0,END))

		if listOfSelected > 10:
			tkm.showerror('Error','Maximum 10 questions per category',parent = self.master)
			

		else:
			if listOfSelected < 10:
				tkm.showwarning('Warning','You need ten questions in a category to start the quiz', parent =self.master)
			# tkm.showinfo('Success','Questions saved', parent =self.master)
				
			with shelve.open('questiondb',writeback = True) as db:
				for questionID in db.keys():
					for selected in range(listOfSelected):
						if db[questionID].entQuestion == self.listRight.get(selected):
							if self.selectedCat not in db[questionID].category:
								db[questionID].category += (self.selectedCat + " ")
					for notSelected in range(listOfNotSelected):
						if db[questionID].entQuestion == self.listLeft.get(notSelected):
							if self.selectedCat in db[questionID].category:
								tStr = db[questionID].category
								tStr = tStr.replace((self.selectedCat + " "),"")
								db[questionID].category = tStr
								
			self.master.destroy()



	def submitButton(self):
		btnSave = Button(self, text='Save selections and close',font=('Helvetica',16))
		btnSave["command"] = self.saveAndQuit
		btnSave.grid(row = 9, column = 7, columnspan =1, sticky = E)

	def leavePage(self):
		btnSave = Button(self, text='Go Back',font=('Helvetica',16))
		btnSave["command"] = self.master.destroy
		btnSave.grid(row = 9, column = 1, columnspan =1, sticky = W)


def main():
	root = Tk()
	root.title("Add Question")
	addQ = addQuestion(root)
	root.mainloop()


# Main
if __name__ == "__main__":
	main()
