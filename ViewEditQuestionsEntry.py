from tkinter import *
from Question import Question
import shelve
from Question import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
import shutil
from Event import Event
import os


class ViewEditQuestions(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createViewEditQuestions()
		self.availableQuestions()
		self.bindListBox()
		self.questionImage()
	   
	def createViewEditQuestions(self):
		
		## Add C U Logo
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row=0, column=0, rowspan =2 )

		## create AdminOptions button

		butAdminOptions = Button(self, text = "Admin Options", font=("MS", 8, "bold"), height=1, width = 15)
		butAdminOptions["command"]=self.master.destroy ## look
		butAdminOptions.grid(row=0, column=8, columnspan=3, sticky = NW, padx=10, pady=5)

		##sets Category title
		lblCategory = Label(self, text = "Category  ", font=("MS", 12, "bold"))    ### Needs coding
		lblCategory.grid(row = 0, column = 1, columnspan = 6, sticky = SW, padx=10, pady=5)

		##sets title
		lblViewEditQuestions = Label(self, text = "View / Edit Questions  ", font=("MS", 14, "bold"))
		lblViewEditQuestions.grid(row = 1, column = 1, columnspan = 6, sticky = NW, padx=10, pady=5)

		# sets currently available label
		lblCurrentlyAvailable = Label(self, text = "(Select From Currently Available Questions)  ", font=("MS", 8, "bold"))
		lblCurrentlyAvailable.grid(row = 3, column = 0, columnspan = 3, sticky = W, padx=10, pady=5)

		#sets up questions listbox
		self.listQ = Listbox(self,height=6, selectmode = SINGLE,bg = "white")
		scroll = Scrollbar(self, command= self.listQ.yview)
		self.listQ.configure(yscrollcommand=scroll.set, exportselection=False)

		#Placed list box next to label and scroll bar after.  Listbox and scrollbar aligned
		#to be next to one another
		self.listQ.grid(row=4, column=0, columnspan=10, sticky=EW, padx=(10,0), pady=5)
		scroll.grid(row=4,column=10,sticky="nsw", rowspan=6)


		#create a labelframe to group q and a

		lblFQandA = LabelFrame(self, bg = "light slate gray")
		lblFQandA.grid(row=10, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)
		#create label for question text box

		lblViewEditQuestion = Label(lblFQandA, text = "Question  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
		lblViewEditQuestion.grid(row = 10, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

		##inserts a text box for question

		self.txtViewEditQuestion = Entry(lblFQandA,  width = 70)
		self.txtViewEditQuestion.grid(row =  11, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

		#create label for answer text box

		lblViewEditAnswer = Label(lblFQandA, text = "Answer  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
		lblViewEditAnswer.grid(row = 12, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

		##inserts a text box for editing question

		self.txtViewEditAnswer = Entry(lblFQandA,  width = 70)
		self.txtViewEditAnswer.grid(row =  13, column = 0, columnspan = 10, sticky = W, padx=10, pady=(1,15))
		
		#create a labelframe to group choices

		lblFChoices = LabelFrame(self, bg = "light slate gray")
		lblFChoices.grid(row=14, column = 0, columnspan = 10, sticky = W, padx=10, pady=15)
		#create label for Choices text boxes

		lblViewEditChoices = Label(lblFChoices, text = "Choices  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
		lblViewEditChoices.grid(row = 14, column = 0, columnspan = 9, sticky = W, padx=10, pady=10)

		##inserts a text box for adding a choice1

		self.txtViewEditChoice1 = Entry(lblFChoices,  width = 70)
		self.txtViewEditChoice1.grid(row =  15, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

	   ##inserts a text box for adding a choice2

		self.txtViewEditChoice2 = Entry(lblFChoices,  width = 70)
		self.txtViewEditChoice2.grid(row =  16, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

	##inserts a text box for adding a choice3

		self.txtViewEditChoice3 = Entry(lblFChoices,  width = 70)
		self.txtViewEditChoice3.grid(row =  17, column = 0, columnspan = 10, sticky = W, padx=10, pady=(5,15))

		## create Clear Add button

		butClearEdit = Button(self, text = "Undo Edits", font=("MS", 8, "bold"), height=1, width = 15)
		butClearEdit["command"] = self.clearEdit
		butClearEdit.grid(row=18, column=0, columnspan=2, sticky = W, padx=10, pady=5)

		## create AddAndUpdate button

		butSaveAndUpdate = Button(self, text = "Save and Update", font=("MS", 8, "bold"), height=1, width = 15, fg = "white", bg = "blue")
		butSaveAndUpdate["command"]=self.saveAndUpdate  
		butSaveAndUpdate.grid(row=18, column=9, columnspan=2, sticky = E, padx=10, pady=5)


		self.butDeleteQuestion  = Button(self, text = "Delete Question", font=("MS", 8, "bold"), height=1, width = 15)
		self.butDeleteQuestion["command"] = self.deleteQuestion
		self.butDeleteQuestion["state"] = "disabled"
		self.butDeleteQuestion.grid(row = 18, column = 6,columnspan = 2)
	
	def deleteQuestion(self):
		if tkm.askyesno("Proceed","Are you sure you want to delete this question?",parent = self.master):
			with shelve.open('questiondb' ,writeback = True) as db:
				for qId in db.keys():
					if db[qId].entQuestion == self.txtViewEditQuestion.get():
						del db[qId]

					
			self.availableQuestions()

	def bindListBox(self):
		self.listQ.bind('<<ListboxSelect>>', self.fillTextBox)

		
		##insert available questions



	def populateButtons(self):
		
          
		self.lblFile = Label(self,text=self.file_name, font=('Helvetica',8,'bold'))
		self.lblFile.grid(row=19,column = 4,columnspan=2)

		self.btnClearImage = Button(self,text='remove', font=('Helvetica',8))
		self.btnClearImage['command'] = self.clearImagePath
		self.btnClearImage.grid(row =19, column=6)

	def questionImage(self):
		# add image to question button
		self.btnImage = Button(self, text='Add Image', font=('Helvetica',8,'bold'),state = "disabled")
		self.btnImage.grid(row = 18, column = 4,columnspan=2)
		self.btnImage['command'] = self.getImagePath

	def getImagePath(self):
		
		self.removeButtons()
		
		#Need to check it's an image in gif format, or convert it (PIL)
		self.file_path = tkf.askopenfilename(parent = self.master)
		if self.file_path != 0:
			
			self.file_name = os.path.basename(self.file_path)	
			self.lblFile = Label(self,text=self.file_name, font=('Helvetica',8,'bold'))
			self.lblFile.grid(row=19,column = 4,columnspan=2)

			self.btnClearImage = Button(self,text='remove', font=('Helvetica',8))
			self.btnClearImage['command'] = self.clearImagePath
			self.btnClearImage.grid(row =19, column=6)
	def removeButtons(self):
		try:
			self.lblFile.grid_forget()
		except AttributeError:
			print("no file label")
		try:
			self.btnClearImage.grid_forget()
		except AttributeError:
			print("Image label and button haven't been created yet but it doesn't matter")
	
	def clearImagePath(self):
		self.file_path=''
		self.removeButtons()
		

	def availableQuestions(self):
		#this should pull questions from shelve file
		self.listQ.delete(0,END)
		with shelve.open('questiondb') as avail:
			klist = list(avail.keys())
			for questionID in klist:
				questionText = avail[questionID].entQuestion
				self.listQ.insert(END,questionText)
				print(questionText)
				
		
	def clearEdit(self):
		#clears all text boxes
		self.txtViewEditChoice1.delete(0,END)
		self.txtViewEditChoice2.delete(0,END)
		self.txtViewEditChoice3.delete(0,END)
		self.txtViewEditQuestion.delete(0,END)
		self.txtViewEditAnswer.delete(0,END)
		self.clearImagePath()
		
	def fillTextBox(self,listQ):
		#clears first
		self.clearEdit()
		#adds to question box
		#adds to other boxes if matched

		with shelve.open('questiondb') as avail:
			for questionID in avail.keys():
				if  avail[questionID].entQuestion ==  self.getAnchor():
					question = avail[questionID].entQuestion
					answer = avail[questionID].entAnswer
					choice1 = avail[questionID].entA1
					choice2 = avail[questionID].entA2
					choice3 = avail[questionID].entA3
					category = avail[questionID].category
					self.txtViewEditQuestion.insert(END,question)
					self.txtViewEditAnswer.insert(END,answer)
					self.txtViewEditChoice1.insert(END,choice1)
					self.txtViewEditChoice2.insert(END,choice2)
					self.txtViewEditChoice3.insert(END,choice3)
					self.file_name = avail[questionID].imageExt
					if self.file_name != "":
						self.populateButtons()
					# self.populateButtons(avail[questionID].imageExt)
		if Event.getCategory() not in category:
			self.butDeleteQuestion["state"] = "normal"
		self.btnImage["state"] = "normal"
			
	def getAnchor(self):
		test = self.listQ.get("anchor")
		return test
						
							
	def saveAndUpdate(self):
		#checks which question has been edited and saves new version (changed or otherwise)
		Q = self.txtViewEditQuestion
		A = self.txtViewEditAnswer
		A1 = self.txtViewEditChoice1
		A2 = self.txtViewEditChoice2
		A3 = self.txtViewEditChoice3


		strMsg = "All boxes must be completed"

		if Q.get() != "" and A.get()!="" and A1.get() != "" and A2.get() !="" and A3.get() !="":    
			with shelve.open('questiondb', writeback=True) as avail:
				for questionID in avail.keys():
					if  avail[questionID].entQuestion ==  self.getAnchor():
						avail[questionID].entQuestion = Q.get() 
						avail[questionID].entAnswer =  A.get()
						avail[questionID].entA1 = A1.get()
						avail[questionID].entA2 = A2.get()
						avail[questionID].entA3 = A3.get()
						avail[questionID].imageExt = self.file_name
						# avail[questionID].imageExt = self.file_path
						# avail.sync
						# avail.close
			if self.file_path != '':
				try:
					local_images = 'Images/'	
					shutil.copy(self.file_path,local_images)
				except shutil.SameFileError:
					pass;
			tkm.showinfo("Success","Question Saved", parent = self.master)
			self.clearEdit()
			self.availableQuestions()
		else:
			tkm.showwarning("Error",strMsg,parent= self.master)

   
def main():
	#main
	root = Tk()  # call the Tk method
	root.title("View/Edit Questions") # set the title
	app= ViewEditQuestions(root)    # creates a new instance of the ViewEditQuestions class
	root.mainloop()  # starts window with mainloop method

