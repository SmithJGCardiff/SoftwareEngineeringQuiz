
from lib.loginDetails import loginDetails
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf


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
		adminButton["command"] = self.master.destroy
		adminButton.grid(row=1, column=4, columnspan=1, sticky=W)

	def questionText(self):
		self.qCount = 1
		lblQuestNum = Label(self, text = ("Question "+str(self.qCount)),font=('Helvetica',32))
		lblQuestNum.grid(row = 2, column = 2, columnspan =2, sticky = EW+S)




		self.lblPic = Label(self, text = self.selectedCategory)
		self.lblPic.grid(row = 3, column = 2, columnspan = 2, rowspan = 2, sticky = EW + NS)

		self.lblQText = Label(self)
		self.lblQText.grid(row = 5, column = 2, columnspan = 2)

		self.lblA1Text = Label(self)
		self.lblA1Text.grid(row = 6, column = 2)

		self.lblA2Text = Label(self)
		self.lblA2Text.grid(row = 6, column = 3)

		self.lblA3Text = Label(self)
		self.lblA3Text.grid(row = 7, column = 2)

		self.lblA4Text = Label(self)
		self.lblA4Text.grid(row = 7, column = 3)

		self.btnCheckAns = Button(self,text = "Check My Answer")
		self.btnCheckAns.grid(row = 8, column = 2, columnspan = 2)

		self.btnResetQuiz = Button(self, text = "Reset the Quiz")
		self.btnResetQuiz.grid(row = 9, column = 2, columnspan = 2)


	# get all ids and populate list then pass list to function ten times to populate questions, need event listener
	def populateText(self,):
		with shelve.open('questiondb','r') as db:
			for questionID in db.keys():
				if self.selectedCategory in db[questionID].category:


def main(selCat):
	root = Tk()
	root.title("Quiz")
	mainQuizWindow(root,selCat)
	root.mainloop()

if __name__ == "__main__":
	main()