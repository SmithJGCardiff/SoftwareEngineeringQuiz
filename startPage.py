from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
from lib import *
import random
from loginWindow import loginWindow
from lib.loginDetails import loginDetails
class startPage(Frame):

	def __init__(self,master, selCat= ""):

		Frame.__init__(self, master)
		self.master = master
		self.grid()
		self.logo()
		self.header()
		self.adminBtn()
		self.welcomeFact()
		self.frontImage()
		self.startTheQuiz()

	def logo(self):			
		# Adds the university logo to the top left corner
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row=1, column=1,rowspan=2 )

	def header(self):
		# Category Name and Window title

		lblWelcome = Label(self, text='Croeso! Welcome!', font=('Helvetica',16))
		lblWelcome.grid(row=1, column=2, columnspan=2, sticky=W)

	def passToAdmin(self):
		loginBox = Toplevel(self.master)
		loginBox.grab_set()
		loginBox.title('Login')
		loginWindow(loginBox)


		

	def adminBtn(self):
		# Admin Options
		adminButton = Button(self, text='Admin Options',font=('Helvetica',16))
		## Need to add in command for admin button here
		adminButton.grid(row=1, column=7, columnspan=1, sticky=W )
		adminButton['command'] = self.passToAdmin



	def welcomeFact(self):

		with open('facts.txt','r') as f:
			num_of_lines = int(f.readline())
			intR = random.randint(1,num_of_lines-1)
			for i, line in enumerate(f):
				if i == intR:
					strFact = line
					break

		lblFacts = Label(self, text=('FACT: ' + strFact),justify = CENTER, wraplength = 600)
		lblFacts.grid(row=3, column =3, columnspan = 4)

	def frontImage(self):
		photo = PhotoImage(file="Images/front_image.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row=4, column=3,rowspan=2, columnspan=4 )

	def startTheQuiz(self):
		strStart = 'Gather more facts from around the room - then come and ...'

		lblStartQuiz = Label(self, text= strStart, justify= CENTER)
		lblStartQuiz.grid(row = 6, column = 3, columnspan = 4)

		# button needs to be disabled if no category is selected
		btnStartQuiz = Button(self, text = 'Start The Quiz', font = ('System', 32, 'bold'))
		btnStartQuiz.configure(background = 'royal blue',
			borderwidth = 2,
			height = 1,
			highlightthickness = 6,
			overrelief = FLAT, #btn state = disabled,
			highlightbackground = 'blue',
			activebackground = 'medium blue',
			foreground = 'grey',
			cursor = 'cross')
		btnStartQuiz.grid(row = 7, column = 3, columnspan = 4)
def main():
	root = Tk()
	# w= 700
	# h = 480
	# ws = root.winfo_screenwidth()
	# hs = root.winfo_screenheight()
	
	# x = (ws/2) - (w/2)
	# y = (hs/2) - (h/2)

	# root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	root.title('Quiz')
	stPage = startPage(root)
	root.mainloop()

if __name__ == "__main__":
	main()