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
		self.grid(row=0, column=0, sticky=N+S+E+W)
		self.logo()
		self.header()
		self.adminBtn()
		self.availableQuestions()
		self.textQandA()
		self.questionImage()

	def logo(self):
		# Adds the university logo to the top left corner
		logoCanvas = Canvas(self, width=150, height=149)
		logoCanvas.grid(row=1, column=1, rowspan=2, sticky=NE)

		self.logo = PhotoImage(file="Images/logo.gif")
		self.logo = self.logo.zoom(15)
		self.logo = self.logo.subsample(70)
		logoCanvas.create_image(75,75,image=self.logo)

	def header(self):
		# Category Name and Window title
		lblHeader = Label(self, text='Add Questions', font=('Helvetica',32))
		lblHeader.grid(row=2, column=2, columnspan=2, sticky=NW)

		lblCatHeader = Label(self, text='Category Name', font=('Helvetica',16))
		lblCatHeader.grid(row=1, column=2, columnspan=2, sticky=SW)

	def adminBtn(self):
		# Admin Options
		adminButton = Button(self, text='Admin Options',font=('Helvetica',16))
		## Need to add in command for admin button here
		adminButton.grid(row=1, column=7, columnspan=2, sticky=W)

	def availableQuestions(self):

		lblQ = Label(self, text='(Currently Available Questions)',font=('Helvetica',8,'bold'))
		lblQ.grid(row=3, column=1, columnspan=2)

		self.listQ = Listbox(self, height=3)
		scroll = Scrollbar(self, command=self.listQ.yview)
		self.listQ.configure(yscrollcommand=scroll.set)

		self.listQ.grid(row=4, column=1, columnspan=8)
		scroll.grid(row=4,column=8,rowspan=4,sticky=W)

		#this should pull questions from shelve file
		with shelve.open('questiondb') as db:
			klist = list(db.keys())
			for questionID in klist:
				questionText = db[questionID].entQuestion
				self.listQ.insert(END,questionText)

		self.listQ.selection_set(END)

		self.listQ.config(width=70)


	def textQandA(self):

		correctQA = LabelFrame(self,padx=5,pady=5,bg='light slate gray')
		correctQA.grid(row=8,column=1,columnspan=8)

		lblQuestion = Label(correctQA,text='Question:',font=('Helvetica',8,'bold'),padx=5,pady=5,bg='light slate gray',fg='white')
		lblAnswer = Label(correctQA,text='Answer:',font=('Helvetica',8,'bold'),padx=5,pady=5, bg='light slate gray',fg='white')

		self.entQuestion = Entry(correctQA,width= 70)
		self.entAnswer = Entry(correctQA, width=70)

		lblQuestion.grid(row=1,column=1,sticky=W)
		self.entQuestion.grid(row=2,column=1,columnspan=2)
		lblAnswer.grid(row=3,column=1,sticky=W)
		self.entAnswer.grid(row=4,column=1,columnspan=2)


		wrongAs = LabelFrame(self,text='Choices:',padx=5,pady=5,bg='light slate gray')
		wrongAs.grid(row=9,column=1,columnspan=8)

		self.entA1 = Entry(wrongAs,width= 70)
		self.entA2 = Entry(wrongAs,width= 70)
		self.entA3 = Entry(wrongAs,width= 70)

		lblA1 = Label(wrongAs,text='Answer 1',font=('Helvetica',8,'bold'),padx=5,pady=5, bg='light slate gray',fg='white')
		lblA2 = Label(wrongAs,text='Answer 2',font=('Helvetica',8,'bold'),padx=5,pady=5, bg='light slate gray',fg='white')
		lblA3 = Label(wrongAs,text='Answer 3',font=('Helvetica',8,'bold'),padx=5,pady=5, bg='light slate gray',fg='white')
		lblA1.grid(row=1,column=1,sticky=W)
		self.entA1.grid(row=2,column=1,columnspan=2)
		lblA2.grid(row=3,column=1,sticky=W)
		self.entA2.grid(row=4,column=1,columnspan=2)
		lblA3.grid(row=5,column=1,sticky=W)
		self.entA3.grid(row=6,column=1,columnspan=2)

		btnSubmit = Button(self, text='Save Question', font=('Helvetica',8,'bold'))
		btnSubmit['command'] = self.storeQuestion
		btnSubmit.grid(row=10,column=6,columnspan=2)

		btnClear = Button(self, text='Clear Question', font=('Helvetica',8,'bold'))
		btnClear['command'] = self.clearQuestion
		btnClear.grid(row=10,column=0,columnspan=2)

	def clearQuestion(self):	
		#clear the question boxes
		self.entQuestion.delete(0,END)
		self.entAnswer.delete(0,END)
		self.entA1.delete(0,END)
		self.entA3.delete(0,END)
		self.entA2.delete(0,END)
		self.clearImagePath()

	def storeQuestion(self):
		strMsg = ""
		if len(self.entQuestion.get()) == 0:
			strMsg += "You have to enter text to save a question. \n"
		if len(self.entAnswer.get()) == 0:
			strMsg += "You have to provide a correct answer to the question. \n"
		if (len(self.entA1.get())==0) and (len(self.entA2.get())==0) and (len(self.entA3.get())==0):
			strMsg += "You have to provide at least 1 alternate answer. \n"
		
		if strMsg =="":
			local_images = 'Images/'	
			shutil.copy(self.file_path,local_images)
			with shelve.open('questiondb') as db:
				if len(db) != 0:
					previousID = max(key for key, value in db.items())
					questionID = int(previousID) + 1
				else:
					questionID = 1

				newQuest = Question(str(questionID),
					'','include topics here',self.entQuestion.get(),
					self.entAnswer.get(),self.entA1.get(),
					self.entA2.get(),self.entA3.get(),
					'')
				db[newQuest.questionID] = newQuest
			tkm.showinfo('Add Question', 'Question Added')
			self.clearQuestion()
			self.clearImagePath()
			self.availableQuestions()


		else:
			tkm.showwarning("Error",strMsg)

	def getImagePath(self):
		#Need to check it's an image in gif format, or convert it (PIL)
		self.file_path = tkf.askopenfilename()
		if self.file_path != 0:
			file_name = os.path.basename(self.file_path)			
			self.lblFile = Label(self,text=file_name, font=('Helvetica',8,'bold'))
			self.lblFile.grid(row=11,column = 2,columnspan=2)

			self.btnClearImage = Button(self,text='remove', font=('Helvetica',8))
			self.btnClearImage['command'] = self.clearImagePath
			self.btnClearImage.grid(row =11, column=4)

	def questionImage(self):
		# add image to question button
		btnImage = Button(self, text='Add Image', font=('Helvetica',8,'bold'))
		btnImage.grid(row = 10, column = 2,columnspan=2)
		btnImage['command'] = self.getImagePath


	def clearImagePath(self):
		self.file_path=''
		try:
			self.lblFile.grid_forget()
			self.btnClearImage.grid_forget()
		except AttributeError:
			print("Image label and button haven't been created yet but it doesn't matter")


	def submitButton(self):
		pass



# Main
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

root.title("View/Edit Questions")
root.configure(background="gray80")
addQ = addQuestion(root)
root.mainloop()