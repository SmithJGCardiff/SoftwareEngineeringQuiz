
from lib.loginDetails import loginDetails
from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf

class loginWindow(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.master = master
		self.grid()
		self.logo()
		self.loginInput()
		self.master.bind("<Return>", self.enterLogin)
		self.entUsername.focus_set()



		
	def logo(self):
		# Adds the university logo to the top left corner
		photo = PhotoImage(file="Images/logo.gif")
		labelLogo = Label(self,image = photo)
		labelLogo.image=photo
		labelLogo.grid(row = 1, column = 1, columnspan = 2)

	def loginInput(self):

		lblUsername = Label(self, text = 'Username: ')
		lblUsername.grid(row = 2, column = 1)

		self.entUsername = Entry(self)
		self.entUsername.grid(row = 2, column = 2)

		lblPassword = Label(self, text = 'Password: ')
		lblPassword.grid(row = 3, column = 1)

		self.entPassword = Entry(self, show = "*")
		self.entPassword.grid(row = 3, column = 2)


		self.btnSubmit = Button(self, text = 'Enter Login Details', command = self.validateLogin)
		self.btnSubmit.grid(row = 4, column = 1, columnspan = 2)

		btnCancel = Button(self, text = 'Cancel', command = self.cancelLogin)
		btnCancel.grid(row = 5, column = 1, columnspan = 2)

	def enterLogin(self,event):
		self.validateLogin()

	def validateLogin(self):
		username = self.entUsername.get()
		password = self.entPassword.get()
		strLogAttempt = loginDetails.check(username, password)
		print(strLogAttempt)
		if strLogAttempt == "login successful":

			self.master.master.destroy()
			import AdminOptions
			AdminOptions.main()
		else:
			tkm.showerror('Login Denied',strLogAttempt)
			


	def cancelLogin(self):
		self.master.destroy()



if __name__ == "__main__":
	root = Tk()
	loginWindow(root)
	root.mainloop()