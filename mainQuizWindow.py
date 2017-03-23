
from lib.loginDetails import loginDetails
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
import shelve
import random

class mainQuizWindow(Frame):

	def __init__(self, master,selCat = ""):

		Frame.__init__(self, master)
		self.selectedCategory = selCat
		self.master = master
		self.grid()
		self.logo()
		self.adminBtn()
		self.questionText()


		
	def logo(self):
        ## create logo
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row=1, column=1, rowspan =2 )

	def adminBtn(self):
		# Admin Options
		adminButton = Button(self, text='Admin Options',font=('Helvetica',16))
		adminButton["command"] = self.passToAdmin
		adminButton.grid(row=1, column=4, columnspan=1, sticky=W)

	def questionText(self):





		listOfStuff = self.populateText()
		random.shuffle(listOfStuff)
		self.qNum = 0

		self.displayQuestion()



		lblQuestNum = Label(self, text = ("Question "+str(self.qNum+1)),font=('Helvetica',32))
		lblQuestNum.grid(row = 2, column = 2, columnspan =2, sticky = EW+S)
	

		


			

			

		answerArray = [(2,"Ans"),(3,"A1"),(4,"A2"),(5,"A3")] 
		random.shuffle(answerArray)


		self.lblPic = Label(self, text = listOfStuff[self.qNum][6])
		self.lblPic.grid(row = 3, column = 2, columnspan = 2, rowspan = 2, sticky = EW + NS)

		self.lblQText = Label(self, text = listOfStuff[self.qNum][1] )
		self.lblQText.grid(row = 5, column = 2, columnspan = 2)

		self.selected = StringVar()
		
		position = [[6,2],[6,3],[7,2],[7,3]]
		count = 0


		for ansNum, ansHidden in answerArray:
			
			btnA = Radiobutton(self,text = listOfStuff[self.qNum][answerArray[count][0]], variable=self.selected,value=ansHidden,indicatoron=0, font=("MS", 8, "bold"),height=2, width = 25)
			btnA.grid(row = position[count][0], column = position[count][1])
			count +=1


		self.btnCheckAns = Button(self,text = "Check My Answer")
		self.btnCheckAns["command"] = self.checkAnswer
		self.btnCheckAns.grid(row = 8, column = 2, columnspan = 2)

		self.btnResetQuiz = Button(self, text = "Reset the Quiz")
		self.btnResetQuiz.grid(row = 9, column = 2, columnspan = 2)

		self.qNum +=1


	def displayQuestion(self):
		if self.qNum == 9:
			print("end of quiz")
		# destroy objects first then repopulate
		destroyObjects()
		# show new question


	def destroyObjects(self):
		pass

	def questionCorrect(self):
		# create label top
		# label tick 
		# update label correct score
		#change button to 

		displayQuestion()


	def checkAnswer(self):
		if self.selected.get() == "Ans":
			print("Correct")

			# update questions and score
			#pass to questioncorrect

		else:
			print("Unlucky")

	# get all ids and populate list then pass list to function ten times to populate questions, need event listener
	def populateText(self,):
		with shelve.open('questiondb','r') as db:
			listOfQs = []
			for questionID in db.keys():
				quiz = db[questionID]


				if self.selectedCategory in db[questionID].category:
					self.questionID = quiz.questionID
					self.questionText = quiz.entQuestion
					self.correctAnswer = quiz.entAnswer
					self.answer1 = quiz.entA1
					self.answer2 = quiz.entA2
					self.answer3 = quiz.entA3
					self.imageLine = quiz.imageExt
					listOfQs.append([self.questionID,self.questionText,self.correctAnswer,self.answer1,self.answer2,self.answer3,self.imageLine])
			return listOfQs


	def passToAdmin(self):
		loginBox = Toplevel(self.master)
		loginBox.grab_set()
		loginBox.title('Login')
		from loginWindow import loginWindow
		loginWindow(loginBox)

def main(selCat):
	root = Tk()
	root.title("Quiz")
	mainQuizWindow(root,selCat)
	root.mainloop()

if __name__ == "__main__":
	main()