
from lib.loginDetails import loginDetails
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
import shelve
import random
from Event import Event
class mainQuizWindow(Frame):

	def __init__(self, master,school):

		Frame.__init__(self, master)
		self.school = school
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
		self.selectedCategory = Event.getCategory()
		self.scoreCount = 0
		self.lblScore = Label(self, text="Current Score \n"+str(self.scoreCount)+"/10", font=('Helvetica', 16))
		self.lblScore.grid(row = 3,column =1)
		self.listOfStuff = self.populateText()
		random.shuffle(self.listOfStuff)
		self.qNum = 0

		self.lblQuestNum = Label(self, text = ("Question "+str(self.qNum+1)+" of 10"),font=('Helvetica',32))
		self.lblQuestNum.grid(row = 2, column = 2, columnspan =2, sticky = EW+S)

		self.answerArray = [(2,"Ans"),(3,"A1"),(4,"A2"),(5,"A3")] 
		random.shuffle(self.answerArray)

		self.lblPic = Label(self, text = self.listOfStuff[self.qNum][6])
		self.lblPic.grid(row = 3, column = 2, columnspan = 2, rowspan = 2, sticky = EW + NS)

		self.lblQText = Label(self, text = self.listOfStuff[self.qNum][1] )
		self.lblQText.grid(row = 5, column = 2, columnspan = 2)

		self.selected = StringVar()

		self.btnA =  Radiobutton(self,text = self.listOfStuff[self.qNum][self.answerArray[0][0]], variable=self.selected,value=self.answerArray[0][1],indicatoron=0, font=("MS", 8, "bold"),height=2, width = 25)
		self.btnA1 = Radiobutton(self,text = self.listOfStuff[self.qNum][self.answerArray[1][0]], variable=self.selected,value=self.answerArray[1][1],indicatoron=0, font=("MS", 8, "bold"),height=2, width = 25)
		self.btnA2 = Radiobutton(self,text = self.listOfStuff[self.qNum][self.answerArray[2][0]], variable=self.selected,value=self.answerArray[2][1],indicatoron=0, font=("MS", 8, "bold"),height=2, width = 25)
		self.btnA3 = Radiobutton(self,text = self.listOfStuff[self.qNum][self.answerArray[3][0]], variable=self.selected,value=self.answerArray[3][1],indicatoron=0, font=("MS", 8, "bold"),height=2, width = 25)
			
		self.btnA.grid(row = 6, column = 2)
		self.btnA1.grid(row = 6, column = 3)
		self.btnA2.grid(row = 7, column = 2)
		self.btnA3.grid(row = 7, column = 3)

		self.btnCheckAns = Button(self,text = "Check My Answer")
		self.btnCheckAns["command"] = self.checkAnswer
		self.btnCheckAns.grid(row = 8, column = 2, columnspan = 2)

		self.btnResetQuiz = Button(self, text = "Reset the Quiz")
		self.btnResetQuiz["command"] = self.endOfQuiz
		self.btnResetQuiz.grid(row = 9, column = 2, columnspan = 2)

		self.lblCorrect = Label(self)
		self.lblCorrect.grid(row = 1, column = 2, columnspan  =2)


	def displayQuestion(self):
		if self.qNum == 9:
			self.endOfQuiz()
			return

		self.btnCheckAns["text"] = "Check my Answer"

		self.btnCheckAns["command"] = self.checkAnswer

		self.qNum +=1
		self.lblCorrect["text"] = ""
		random.shuffle(self.answerArray)
		self.lblQuestNum["text"] = ("Question "+str(self.qNum+1)+" of 10")
		self.lblPic["text"] = self.listOfStuff[self.qNum][6]
		self.lblQText["text"] = self.listOfStuff[self.qNum][1]
		self.btnA["text"] = self.listOfStuff[self.qNum][self.answerArray[0][0]]
		self.btnA1["text"] = self.listOfStuff[self.qNum][self.answerArray[1][0]]
		self.btnA2["text"] = self.listOfStuff[self.qNum][self.answerArray[2][0]]
		self.btnA3["text"] = self.listOfStuff[self.qNum][self.answerArray[3][0]]
		self.btnA["value"] = self.answerArray[0][1]
		self.btnA1["value"] =  self.answerArray[1][1]
		self.btnA2["value"] = self.answerArray[2][1]
		self.btnA3["value"] = self.answerArray[3][1]
		self.selected.set("Raise")

		self.btnA["state"] = "normal" 
		self.btnA1["state"] = "normal"
		self.btnA2["state"] = "normal"
		self.btnA3["state"] = "normal"
		# destroy objects first then repopulate

		# show new question


	def questionCorrect(self):
		# create label top
		# label tick 
		# update label correct score
		#change button to next question which runs display question
		self.lblCorrect["text"] = "Correct"
		
		self.btnCheckAns["command"] = self.displayQuestion
		Event.addQScores(self.listOfStuff[self.qNum][0],"correct",self.school)

	def questionIncorrect(self):

		self.btnCheckAns["command"] = self.displayQuestion
		self.lblCorrect["text"] = "Incorrect"
		Event.addQScores(self.listOfStuff[self.qNum][0],"incorrect",self.school)

	def checkAnswer(self):

		self.btnA["state"] = "disabled" 
		self.btnA1["state"] = "disabled"
		self.btnA2["state"] = "disabled"
		self.btnA3["state"] = "disabled"
		currQID = self.listOfStuff[self.qNum][0]
		self.btnCheckAns["text"] = "Next Question"
		if self.qNum == 9:
			self.btnCheckAns["text"] = "End Quiz"
			self.btnCheckAns["command"] = self.endOfQuiz
			self.btnResetQuiz["state"] = "disabled"


		if self.selected.get() != "Ans":
			print("Unlucky")
			self.questionIncorrect()

			# open shelve file and find question id and score a mark against it
			# whith shelve.open()

		else:
			print("Correct")
			self.questionCorrect()
			self.scoreCount+=1
			self.lblScore["text"] = "Current Score \n"+str(self.scoreCount)+"/10"
			# open shelve and score mark against incorrect

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

	def endOfQuiz(self):
		self.lblQuestNum["text"] = "Well Done!"
		self.lblPic["text"] = "Your score this time was: "
		self.lblQText["text"] = str(self.scoreCount)+" / 10"
		self.btnCheckAns["text"] = "Restart the quiz"
		self.btnA1.grid_forget()
		self.btnA2.grid_forget()
		self.btnA3.grid_forget()
		self.btnA.grid_forget()
		self.lblCorrect.grid_forget()
		self.lblScore.grid_forget()
		self.btnCheckAns["command"] = self.restartQuiz

		self.btnResetQuiz.grid_forget()
		# save quiz here 
		
	def restartQuiz(self):

		if self.qNum < 10:
			qIDList = []
			for i in range(self.qNum+1,10):
				Event.addQScores(self.listOfStuff[i][0],"unanswered",self.school)

		import startPage
		self.master.destroy()
		startPage.main()

	def passToAdmin(self):
		loginBox = Toplevel(self.master)
		loginBox.grab_set()
		loginBox.title('Login')
		from loginWindow import loginWindow
		loginWindow(loginBox)

def main(school):
	root = Tk()
	root.title("Quiz")
	mainQuizWindow(root,school)
	root.mainloop()

if __name__ == "__main__":
	main()