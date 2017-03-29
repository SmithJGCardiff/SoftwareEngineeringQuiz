
#*** Imports ***
from tkinter import *
from tkinter import messagebox as tkm

import shelve
import sys
import os
import time
from Event import Event
#--------------------------------------------------------------------------------------------------------------
#import AdminOptions
import View_Stats






#*** Classes ***
class Manage_Stats(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()

		# self.grid_columnconfigure(0, minsize=200)
		# self.grid_rowconfigure(0, minsize=200)
		
		self.event_entry = Entry(self,width=17,font=('Lato',13,'bold'))
		self.school_entry = Entry(self,width=20,font=('Lato',13,'bold'))
		self.school_list = Listbox(self,height=5,width=8,bg='white',font=('Lato',13,'bold'),selectmode=MULTIPLE)
		
		self.create_interface()

#--------------------------------------------------------------------------------------------------------------

	def create_interface(self):
		
		#*** Cardiff University Logo ***
		logo = PhotoImage(file="Images/logo.gif")
		CU_logo = Label(self,image=logo)
		CU_logo.image = logo
		CU_logo.grid(row=0,column=0,sticky=NW,padx=(20,0))
		CU_logo.grid_rowconfigure(0, weight=1)
		CU_logo.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Create Admin Options button ***
		admin_button = Button(self,text="Admin Options",font=('Lato',11,'bold'),bg='Gray',fg='black',height=1,width=15,command=self.admin_options)
		admin_button.bind("<Button-1>")
		admin_button.grid(row=0,column=14,ipadx=10,ipady=7,sticky=NE)
		admin_button.grid(rowspan=2,columnspan=2)
		admin_button.config(highlightbackground='black')
		admin_button.grid_rowconfigure(0, weight=1)
		admin_button.grid_columnconfigure(0, weight=1)	

#--------------------------------------------------------------------------------------------------------------

		#*** Page title ***
		page_title = Label(self, text="Manage Statistics",font=("Lato",25,"bold"))
		page_title.grid(row=0,column=1,sticky=W)
		page_title.grid_rowconfigure(0, weight=1)
		page_title.grid_columnconfigure(0, weight=1)		

#--------------------------------------------------------------------------------------------------------------

		#*** View Statistics for events button ***
		stats_button = Button(self,text="View statistics for an event",font=('Lato',15,'bold'),height=3,width=30,bg='MediumBlue',fg='white',command=self.view_stats)
		stats_button.bind("<Button-1>")
		stats_button.grid(row=2,column=9,padx=5,pady=2,ipadx=7,ipady=3)
		stats_button.grid(rowspan=2,columnspan=3)
		stats_button.grid_rowconfigure(0, weight=1)
		stats_button.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Refresh quiz for new event button ***

		refresh_button = Button(self,text="Refresh quiz for new event",font=('Lato',15,'bold'),height=3,width=30,bg='red',fg='white',command=self.refresh_quiz)
		refresh_button.bind("<Button-1>")

		refresh_button.grid(row=5,column=9,padx=5,pady=20,ipadx=7,ipady=3)
		refresh_button.grid(rowspan=2,columnspan=3)
		refresh_button.grid_rowconfigure(0, weight=1)
		refresh_button.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Enter name of a new event ***
		event_name = Label(self, text="Name of new event: ",font=("Lato",17,"bold"),fg='black',bd=3,height=2,width=25)
		event_name.grid(row=7,column=10,pady=30)
		event_name.grid(rowspan=2)
		event_name.grid_rowconfigure(0, weight=1)
		event_name.grid_columnconfigure(0, weight=1)

		self.event_entry.grid(row=7,column=11,sticky=W)  
		self.event_entry.grid(rowspan=2)  	
		self.event_entry.grid_rowconfigure(0, weight=1)
		self.event_entry.grid_columnconfigure(0, weight=1)		

#--------------------------------------------------------------------------------------------------------------

		#*** Select school from school list***
		school_prompt = Label(self,text="Select participating schools: ",font=('Lato',17,'bold'),fg='black',bd=3,height=2,width=35)
		school_prompt.grid(row=9,column=10)
		school_prompt.grid_rowconfigure(0, weight=1)
		school_prompt.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Listbox with school names ***
		scroll = Scrollbar(self,command= self.school_list.yview)	
		scroll.grid(row=10, column=12, sticky=NS,rowspan=2)
		scroll.grid_rowconfigure(0, weight=1)
		scroll.grid_columnconfigure(0, weight=1)		
		
		self.school_list.configure(yscrollcommand=scroll.set)
		self.school_list.grid(row=10, column=9, rowspan=2,columnspan=3,sticky=EW,padx=5, pady=2)
		self.school_list.grid_rowconfigure(0, weight=1)
		self.school_list.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Loading the school names in the listbox ***
		with shelve.open('schoolsdb','c') as db:
			if "Schools" in db.keys():
				schools_list = db['Schools']

			else:
				schools_list = ["No schools currently"]

		for school in sorted(schools_list):
			self.school_list.insert(END, school)


		
#--------------------------------------------------------------------------------------------------------------

		#*** Enter a new school name to the school list ***
		new_school_name = Label(self, text="Add new school to the list: ",font=("Lato",17,"bold"),fg='black',bd=3,height=2,width=25)
		new_school_name.grid(row=12,column=10,pady=30)
		new_school_name.grid(rowspan=2)  
		new_school_name.grid_rowconfigure(0, weight=1)
		new_school_name.grid_columnconfigure(0, weight=1)		
	
		self.school_entry.grid(row=12,column=11,sticky=W)
		self.school_entry.grid(rowspan=2)  
		self.school_entry.grid_rowconfigure(0, weight=1)
		self.school_entry.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Add new school button ***		
		add_school_button = Button(self,text="Add new school",font=('Lato',12,'bold'),height=1,width=15,bg='MediumBlue',fg='white',command=self.add_school)
		add_school_button.bind("<Button-1>")
		add_school_button.grid(row=12,column=13,padx=5,pady=2,ipadx=5,ipady=2)
		add_school_button.grid(rowspan=2)
		add_school_button.grid_rowconfigure(0, weight=1)
		add_school_button.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Save event button ***
		save_event_button = Button(self,text="Save event",font=('Lato',15,'bold'),height=3,width=30,bg='MediumBlue',fg='white',command=self.save_event)
		save_event_button.bind("<Button-1>")
		save_event_button.grid(row=14,column=10,padx=5,pady=30,ipadx=7,ipady=3)
		save_event_button.grid(rowspan=2,columnspan=3)	
		save_event_button.grid_rowconfigure(0, weight=1)
		save_event_button.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

	#*** Class methods ***

	def admin_options(self):
		""" Login to admin menu. Grant access only to authorised users. """
		import AdminOptions
		self.master.destroy()
		AdminOptions.main()
		#os.system('python3 AdminOptions.py') THIS IS GOING TO EXECUTE THE ADMIN OPTIONS SCRIPT
#--------------------------------------------------------------------------------------------------------------

	def view_stats(self):
		""" View event statistics """
		
		os.system('python3 View_Stats.py')

#--------------------------------------------------------------------------------------------------------------

	def refresh_quiz(self):
		""" 
		Refreshing quiz leads to clear of all current data. 
		Return user to main menu.
		"""
		# self.warning_message('Pressing refresh button will delete current data')

		with shelve.open('eventslogdb','c') as db:
			if "currentEvent" in db.keys():
				currentEvent = db["currentEvent"]
				del db["currentEvent"]
				db[currentEvent.dateTime] = currentEvent

		# os.system('python3 Main_Quiz.py') THIS IS GOING TO EXECUTE THE MAIN MENU QUIZ SCRIPT

#--------------------------------------------------------------------------------------------------------------

	def schools_selection(self):
		""" Selects schools from the list and returns a list with the schools participating in the event """

		selected_schools = []
		
		schools = self.school_list.curselection()

		for i in schools:
			chosen_school = self.school_list.get(i)
			selected_schools.append(chosen_school)

		return selected_schools

#--------------------------------------------------------------------------------------------------------------


	def event_date(self):
		'''Returns the date on which the event took place.'''	

		event_date = time.strftime('%A %B %m %G')
		return event_date 

#--------------------------------------------------------------------------------------------------------------

	def save_event(self):
		""" Save event preferences """
		self.refresh_quiz()

		event_name = self.event_entry.get() #Name of the event
		event_date = time.ctime() #The date of the event
		event_schools = self.schools_selection()
		 #The schools tha will participate in the event
		#event_category = [] #The 10 questions selected for the specific event
		


		#LETS SAY WE HAD 4 QUESTIONS. EACH HAS 3 ATTRIBUTES: QUESTION = [times_correct, times_incorrect, times_left]


		questionScores = dict()


		# a = percentages(question_1)
		# b = percentages(question_2)
		# c = percentages(question_3)
		# d = percentages(question_4)

		# category_scores = [a,b,c,d]

		
		if(event_name !=''):
			if(len(event_schools) != 0):
				event_category = ""

				EVENT_DATA = Event(event_name, event_date, event_schools, event_category,questionScores)

				#log = shelve.open('eventslogdb')
				with shelve.open('eventslogdb','c', writeback=True) as db:
					db["currentEvent"] = EVENT_DATA

			else:
				tkm.showerror("Error",'You have to add at least one school for the event!',parent=self.master)
		else:
			tkm.showerror("Error",'You have to enter a name for the event!',parent=self.master)
		

		tkm.showinfo("Event Created","You have created an event, please add a category before starting the quiz",parent = self.master)
		#Clear event entry text field
		self.event_entry.delete(0, 'end')

		# os.system('python3 Main_Quiz.py') THIS IS GOING TO EXECUTE THE MAIN MENU QUIZ SCRIPT


#--------------------------------------------------------------------------------------------------------------
	def warning_message(self,message):
		try:
			messagebox.showinfo('Warning', message)
			answer = messagebox.askquestion('Proceed?','Are you sure?',icon = 'warning')
			if(answer == 'yes'):
				print('refreshed')
			else:
				pass
		except Exception as e:
			print(e)	


	def add_school(self):
		""" Adding a school to the schools list """

		school_name = self.school_entry.get()

		if(school_name != ''):
			with shelve.open('schoolsdb','c') as db:
				if "Schools" in db.keys():
					schools_list = db['Schools']
					if school_name not in schools_list:
						schools_list.append(school_name)
						schools_list = sorted(schools_list)
					else:
						tkm.showerror("Error","School already present",parent = self.master)
				else:
					schools_list = [school_name]
				
				db['Schools'] = schools_list


			self.school_entry.delete(0, END)   # Clear school entry text field

			self.school_list.delete(0, END) #Clear listbox before updating it to avoid doubling of schools

			for school in schools_list:
				self.school_list.insert(END, school)

			
			self.school_entry.update_idletasks() # Update school listbox

#--------------------------------------------------------------------------------------------------------------

def percentages(question):
	total = question[0]+question[1]+question[2]

	percent_correct = float((question[0]/total)*100)
	percent_incorrect = float((question[1]/total)*100)
	percent_left = float((question[2]/total)*100)

	question_scores = [percent_correct,percent_incorrect,percent_left]

	return question_scores

#--------------------------------------------------------------------------------------------------------------



#*** Functions ***		

def main():
	""" Main method - Frame initialisation """


	root = Tk()
	root.title("Manage Statistics")
	app = Manage_Stats(root)


	#*** Get the screen resolution and run the frame in fullscreen. ***
	#width, height = root.winfo_screenwidth(), root.winfo_screenheight()
	#root.geometry('%dx%d+0+0' % (width,height))	

	root.mainloop()




if __name__ == "__main__":
#*** Main Program ***
	main()
	


	
	