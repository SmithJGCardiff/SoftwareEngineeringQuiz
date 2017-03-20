
#*** Imports ***
from tkinter import *
from tkinter import messagebox
import shelve
import sys
import time



#*** Classes ***
class Manage_Stats(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.event_entry = Entry(self)
		self.school_entry = Entry(self)
		self.school_list = Listbox(self,height=5,width=23,bg='white',font=('MS Sans Serif',11))

		self.create_interface()
		# self.view_stats()
		# self.add_school()

	def create_interface(self):
		
		#*** Cardiff University Logo ***
		logo = PhotoImage(file="Images/CU_logo.gif")
		CU_logo = Label(self,image=logo)
		CU_logo.image = logo
		CU_logo.grid(row=0,column=0)


		#*** Create Admin Options button ***
		admin_button = Button(self,text="Admin Options",font=('MS Sans Serif',9,'bold'),height=1,width=15,command=self.admin_options)
		admin_button.bind("<Button-1>")
		admin_button.grid(row=0,column=27,columnspan=2,sticky=NE,padx=2,pady=2)


		#*** Page title ***
		page_title = Label(self, text="Manage Statistics",font=("MS Sans Serif",20,"bold"))
		page_title.grid(row=0,column=7,sticky=W)


		#*** View Statistics for events button ***
		stats_button = Button(self,text="View statistics for an event",font=('MS Sans Serif',11,'bold'),height=3,width=25,bg='MediumBlue',fg='white',command=self.view_stats)
		stats_button.bind("<Button-1>")
		stats_button.grid(row=3,column=20,rowspan=2,columnspan=9,sticky=W,padx=7,pady=1)

		#*** Refresh quiz for new event button ***
		refresh_button = Button(self,text="Refresh quiz for new event",font=('MS Sans Serif',11,'bold'),height=3,width=25,bg='red',fg='white',command=self.refresh_quiz)
		refresh_button.bind("<Button-1>")
		refresh_button.grid(row=5,column=20,rowspan=2,columnspan=9,sticky=W,padx=7,pady=1)

		#*** Warning! Pressing refresh button will delete current data ***
		# command=warning_message('Refresh button will delete all current data',		

		#*** Enter name of a new event ***
		event_name = Label(self, text="Name of new event",font=("MS Sans Serif",15,"bold"),fg='black',bd=3)
		event_name.grid(row=8,column=20)
		#event_entry = Text(self, height=1, width=25)
		self.event_entry.grid(row=9,column=19,rowspan=2,columnspan=5)    	
		

		#*** Select school from school list***
		school_prompt = Label(self,text="Select participant school from the following list of schools",font=('MS Sans Serif',13,'bold'),fg='black',bd=3)
		school_prompt.grid(row=12,column=20)



		#*** Listbox with school names ***
		#self.school_list = Listbox(self,height=5,width=23,bg='white',font=('MS Sans Serif',11))
		scroll = Scrollbar(self,command= self.school_list.yview)
		self.school_list.configure(yscrollcommand=scroll.set)
		self.school_list.grid(row=17, column=20, columnspan=10, sticky=EW,padx=10, pady=5)
		scroll.grid(row=17, column=30, sticky=NS,rowspan=3)


		#*** Loading the school names in the listbox ***
		db = shelve.open('schools.dat')
		schools_list = db['Schools']
		db.close()

		for school in sorted(schools_list):
			self.school_list.insert(END, school)

		self.school_list.selection_set(END)

		



		#*** Enter a new school name to the school list ***
		new_school_name = Label(self, text="Add new school to the list",font=("MS Sans Serif",15,"bold"),fg='black',bd=3)
		new_school_name.grid(row=24,column=20)
		
		#school_entry = Entry(self)
		self.school_entry.grid(row=25,column=19,rowspan=2,columnspan=5)



		#*** Add new school button ***		
		add_school_button = Button(self,text="Add new school",font=('MS Sans Serif',10,'bold'),height=1,width=15,bg='MediumBlue',fg='white',command=self.add_school)
		add_school_button.bind("<Button-1>")
		add_school_button.grid(row=25,column=24,padx=7,pady=1)



		#*** Save event button ***
		save_event_button = Button(self,text="Save event",font=('MS Sans Serif',11,'bold'),height=3,width=25,bg='MediumBlue',fg='white',command=self.save_event)
		save_event_button.bind("<Button-1>")
		save_event_button.grid(row=27,column=20,sticky=W,padx=7,pady=1)	






		






#*** Password authentication window ***


	def admin_options(self):
		""" Login to admin menu. Grant access only to authorised users. """
		access = grant_access()
		print('Admin Options')
		return True


	def view_stats(self):
		""" View event statistics """
		print('View Stats')
		return True


	def refresh_quiz(self):
		""" 
		Refreshing quiz leads to clear of all current data. 
		Return user to main menu.
		"""

		print('refresh quiz')
		return True


	def save_event(self):
		""" Save event preferences """
		event_name = self.event_entry.get()
		self.event_entry.delete(0, 'end')   # Clear event entry text field
		print(event_name)
		print('event saved successfully')
		return True


	def add_school(self):
		""" Adding a school to the schools list """

		school_name = self.school_entry.get()

		if(school_name is not ''):
			db = shelve.open('schools.dat')
			schools_list = db['Schools']
			schools_list.append(school_name)
			schools_list = sorted(schools_list)
			db['Schools'] = schools_list
			db.sync()
			db.close()

			self.school_entry.delete(0, 'end')   # Clear school entry text field

			for school in schools_list:
				self.school_list.insert(END, school)

			self.school_list.selection_set(END)
			
			self.school_entry.update_idletasks() # Update school listbox

			return True

		else:
			return False




		
	# def load_schools(self):	
	# 	""" Loading the school names in the listbox """
	# 	db = shelve.open('schools.dat')
	# 	schools_list = db['Schools']
	# 	db.close()


		



	



#*** Functions ***

def warning_message(text,function):
	try:
		messagebox.showwarning('Warning!','Are you sure about this action?')

	# except tkinter.TclError: #Prevents "can't invoke "grab" command: application has been destroyed" error
	# 	sys.exc_traceback = None 

		prompt_action = messagebox.askquestion(text)

		if(prompt_action == 'yes'):
			return function
		else:
			sys.exit() 

	except Exception as e:
		print(e)

		

def grant_access():
	"""Check and validate password in order to grant access only to authorised users"""
	
	password = "Qu1z_D4y"
	
	try:
		x = input('Please enter password: ')
		
		if(x != password):
			print('Password incorrect.\nAccess denied')
			return grant_access()
		else:
			print('Access granted!')

	except KeyboardInterrupt:
		print("User keyboard interrupt")
		return grant_access()

	sys.exit()





#*** Main Program ***
if __name__ == "__main__":

	root = Tk()
	root.title("Manage Statistics")
	app = Manage_Stats(root)
	

	root.mainloop()



	


	
	