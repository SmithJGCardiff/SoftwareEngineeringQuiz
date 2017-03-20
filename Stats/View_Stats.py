#*** Imports ***
from tkinter import *
from tkinter import messagebox
import shelve
import sys
import time




#*** Classes ***
class View_Stats(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.events_list = Listbox(self,height=5,width=13,bg='white',font=('MS Sans Serif',11))
		self.create_interface()
		# self.view_stats()
		

	def create_interface(self):
		
		#*** Cardiff University Logo ***
		logo = PhotoImage(file="Images/CU_logo.gif")
		CU_logo = Label(self,image=logo)
		CU_logo.image = logo
		CU_logo.grid(row=0,column=0)


		#*** Create Admin Options button ***
		admin_button = Button(self,text="Admin Options",font=('MS Sans Serif',9,'bold'),height=1,width=15,command=self.admin_options)
		admin_button.bind("<Button-1>")
		admin_button.grid(row=0,column=17,columnspan=2,sticky=NE,ipadx=7,ipady=5)


		#*** Page title ***
		page_title = Label(self, text="Manage Statistics",font=("MS Sans Serif",20,"bold"))
		page_title.grid(row=0,column=7,sticky=W,padx=10,pady=5)


		#*** Select event to see statistics ***
		page_title = Label(self, text="Select event to see statistics",font=("MS Sans Serif",12,"bold"))
		page_title.grid(row=7,column=0,sticky=W,padx=10,pady=5)


		#*** Listbox with event names ***
		scroll = Scrollbar(self,command= self.events_list.yview)
		self.events_list.configure(yscrollcommand=scroll.set)
		self.events_list.grid(row=8, column=0, columnspan=4, sticky=EW,padx=10, pady=5)
		scroll.grid(row=8, column=4, sticky=NS,rowspan=3)


		#*** Loading the event names in the listbox. ***
		db = shelve.open('events.dat')
		events = db['Events']
		db.close()
		events = sorted(events)

		for event in events:
			self.events_list.insert(END, event)

		self.events_list.selection_set(END)


		#*** Display statistics for selected event. ***

		self.txtDisplay = Text(self, height=17,width=100)
		self.txtDisplay.tag_configure('boldfont', font=("MS Sans Serif",12,"bold"))
		self.txtDisplay.tag_configure('normfont', font=("MS Sans Serif",12))
		
		

		#*** Event:  Date: ***
		self.txtDisplay.insert(END, 'Event name:  ','boldfont')
		self.txtDisplay.insert(END, 'Cardiff Computing Session' + '\n\n','normfont')
		self.txtDisplay.insert(END, 'Date:  ','boldfont')
		self.txtDisplay.insert(END, 'Wednesday, 15 March' + '\n\n\n','normfont')

		#*** Schools attending: ***
		self.txtDisplay.insert(END, 'Schools attending: ','boldfont' )
		self.txtDisplay.insert(END, 'Ysgol Bro Eirwg, ' + 'Ysgol Glan Ceubal, ' + 'Ysgol Gymraeg Coed-Y-Gof' + '\n\n\n\n','normfont' )
		#*** Questions ***
		self.txtDisplay.insert(END, 'Question' + 5*'\t' + '% Times Correct' + 3*'\t' + '% Times Incorrect' + 3*'\t' + '% Times Left' + '\n\n\n','boldfont' )
	
		questions_list = self.load_questions()
		for question in questions_list:
			self.txtDisplay.insert(END, question + '\n\n','boldfont')


		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.grid(row=25,column=0,sticky=EW)


	def admin_options(self):
		""" Login to admin menu. Grant access only to authorised users. """
		access = grant_access()
		print('Admin Options')

	def load_questions(self):
		db = shelve.open('questions.dat')
		questions = db['Questions']
		db.close()
		return questions




#*** Functions ***

def grant_access():
	""" Check and validate password in order to grant access only to authorised users. """

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
	root.title("View Statistics")
	app = View_Stats(root)
	

	root.mainloop()