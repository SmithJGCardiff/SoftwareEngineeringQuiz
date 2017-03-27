#*** Imports ***
from tkinter import *
from tkinter import messagebox
import shelve
import os
import sys
import time
#--------------------------------------------------------------------------------------------------------------
#import Admin_Options



#*** Classes ***
class View_Stats(Frame):

	def __init__(self, master):
		
		Frame.__init__(self, master)
		self.grid()
		self.events_list = Listbox(self,height=8,width=5,bg='white',font=('Lato',12,'bold'),selectmode=SINGLE)
		self.events_list.bind('<Double-Button-1>',self.display_event_stats)
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
		admin_button = Button(self,text="Admin Options",font=('Lato',11,'bold'),height=1,width=15,bg='Gray',fg='black',command=self.admin_options)
		admin_button.bind("<Button-1>")
		admin_button.grid(row=0,column=14,padx=(180,0),ipadx=10,ipady=7,sticky=NE)
		admin_button.grid(rowspan=2,columnspan=2)
		admin_button.config(highlightbackground='black')
		admin_button.grid_rowconfigure(0, weight=1)
		admin_button.grid_columnconfigure(0, weight=1)	

#--------------------------------------------------------------------------------------------------------------

		#*** Page title ***
		page_title = Label(self, text="Statistics",font=("Lato",25,"bold"))
		page_title.grid(row=0,column=0,padx=(0,65),sticky=E)
		page_title.grid_rowconfigure(0, weight=1)
		page_title.grid_columnconfigure(0, weight=1)		

#--------------------------------------------------------------------------------------------------------------

		#*** Select event to see statistics ***
		select_event = Label(self, text="Select event to see the statistics (double-click): ",font=("Lato",15,"bold"))
		select_event.grid(row=1,column=0,sticky=NW,padx=(20,0),pady=(20,20))
		select_event.grid_rowconfigure(0, weight=1)
		select_event.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Listbox with event names ***
		scroll = Scrollbar(self,command= self.events_list.yview)	
		scroll.grid(row=2, column=1, sticky=NS)
		scroll.grid(rowspan=2)
		scroll.config(highlightbackground='black')
		scroll.grid_rowconfigure(0, weight=1)
		scroll.grid_columnconfigure(0, weight=1)		
		
		self.events_list.configure(yscrollcommand=scroll.set)
		self.events_list.config(highlightbackground='black')
		self.events_list.grid(row=2, column=0, rowspan=2,columnspan=1,sticky=EW,padx=(20,0))
		self.events_list.grid_rowconfigure(0, weight=1)
		self.events_list.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

		#*** Loading the event names in the listbox. ***

		with shelve.open('eventslogdb') as s:
			events = []
			for i in s.keys():
				events.append(i)
			# x = s['EVENT_DATA']
			# #print(x[0])
			# for item in x:
			# 	event_name = item[0]
			# 	#print(event_name)
			# 	events.append(event_name)
			# 	events = sorted(events)

		for event in events:
			self.events_list.insert(END, event)

		self.events_list.selection_set(END)

#--------------------------------------------------------------------------------------------------------------

		#*** Cancel button ***
		cancel_button = Button(self,text="Cancel",font=('Lato',12,'bold'),height=1,width=15,bg='Gray',fg='black',command=self.cancel)
		cancel_button.bind("<Button-1>")
		cancel_button.grid(row=2,column=2,pady=2,ipadx=5,ipady=2,sticky=SW)
		cancel_button.grid(rowspan=2)
		cancel_button.config(highlightbackground='black')
		cancel_button.grid_rowconfigure(0, weight=1)
		cancel_button.grid_columnconfigure(0, weight=1)

	

#--------------------------------------------------------------------------------------------------------------
		
	#*** Get selected event from listbox to display its statistics ***

	def display_event_stats(self,event):
		


		events = self.events_list.curselection()

		selected_event = self.events_list.get(events)


		#print(selected_event)
		table = [0,0,0,0]

		with shelve.open('eventslogdb') as db:
			for key in db.keys():
				#print(key)
				#print(selected_event)
				
				if(selected_event == key):
					
					table[0] = selected_event
					
					table[1] = db[key][1]

					table[2] = "" #Strings with the schools attending initially empty
					for i in db[key][2]: #put all the schools in a string to avoid displaying list brackets
						table[2] = table[2] + ("{}       ".format(i))

					table[3] = db[key][4]
					#print(table[3])
					#print(table[3][1])


#--------------------------------------------------------------------------------------------------------------

		#*** Display statistics for selected event. **
		self.txtDisplay = Text(self, height=40,width=160)
		self.txtDisplay.tag_configure('boldfont', font=("Lato",12,"bold"))
		self.txtDisplay.tag_configure('normfont', font=("Lato",12))
		self.txtDisplay.tag_configure("center", justify='center')	
#--------------------------------------------------------------------------------------------------------------
				
		#*** Event, Date ***
		self.txtDisplay.insert(END, '\n')
		self.txtDisplay.insert(END, '   Event name:  ','boldfont')
		self.txtDisplay.insert(END, ' {}'.format(table[0]) + '\n' + 186 * '-','normfont')
		self.txtDisplay.insert(END, '    Date:  ','boldfont')
		self.txtDisplay.insert(END, ' {}'.format(table[1]) + '\n' + 186 * '-','normfont')
					

#--------------------------------------------------------------------------------------------------------------

		#*** Schools attending: ***
		self.txtDisplay.insert(END, '    Schools attending: ','boldfont' )	
		self.txtDisplay.insert(END, ' {}'.format(table[2]) + '\n'+ 186 * '-','normfont')

		self.txtDisplay.insert(END, '    Category:  ','boldfont')
		self.txtDisplay.insert(END, ' Science & Technology' + '\n' + 186 * '-' + '\n\n','normfont')

#--------------------------------------------------------------------------------------------------------------

		#*** Questions ***
		self.txtDisplay.insert(END, '   Question' + 11*'\t' + '% Times Correct' + 3*'\t' + '% Times Incorrect' + 3*'\t' + '% Times Left' + '\n\n\n','boldfont' )
		
		questions_list = self.load_questions()

		for question in questions_list:
			self.txtDisplay.insert(END, '   ' + question + '\n\n','boldfont')

		self.txtDisplay.insert(END, '   {}'.format('question 1') + 11*'\t' + '{}'.format(table[3][0][0]) + 3*'\t' + '{}'.format(table[3][0][1]) + 3*'\t' + '{}'.format(table[3][0][2]) + '\n\n\n','boldfont' )
#--------------------------------------------------------------------------------------------------------------

		self.txtDisplay.config(state=DISABLED)
		self.txtDisplay.config(highlightbackground='black')
		self.txtDisplay.grid(row=4,column=0,columnspan=10,sticky=EW,padx=(20,0),pady=10)
		self.txtDisplay.grid_rowconfigure(0, weight=1)
		self.txtDisplay.grid_columnconfigure(0, weight=1)	

#--------------------------------------------------------------------------------------------------------------

		#*** Export to CSV button ***
		export_stats = Button(self,text="Export to CSV",font=('Lato',12,'bold'),height=1,width=15,bg='Gray',fg='black',command=self.export_stats)
		export_stats.bind("<Button-1>")
		export_stats.grid(row=4,column=10,padx=5,pady=10,ipadx=5,ipady=2,sticky=SE)
		export_stats.grid(rowspan=2)
		export_stats.config(highlightbackground='black')
		export_stats.grid_rowconfigure(0, weight=1)
		export_stats.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------------------------------------

	def cancel(self):
		self.master.destroy()
		return 'pressed'

	def admin_options(self):
		""" Login to admin menu. Grant access only to authorised users. """

		#os.system('python3 Admin_Options.py') THIS IS GOING TO EXECUTE THE ADMIN OPTIONS SCRIPT


#--------------------------------------------------------------------------------------------------------------

	def load_questions(self):
		""" Load event's questions"""

		filename = 'questionsdb'
		check_file = os.path.isfile(filename)
		
		if(check_file is True): 
			db = shelve.open('questionsdb')
			questions = db['Questions']
			db.close()
			return questions
		
		else:
			file_warning(filename)

#--------------------------------------------------------------------------------------------------------------

	def export_stats(self):
		""" Export statistics to a csv file """

		print('export stats')

#--------------------------------------------------------------------------------------------------------------

#*** Functions ***
def file_warning(filename):
	""" Warn user in case the file he tries to open is not in the directory. """
	
	try:
		messagebox.showwarning('Warning! File {} not found in directory.'.format(filename))

	except Exception as e:
		print(e)

#--------------------------------------------------------------------------------------------------------------

def main():
	""" Main method - Frame initialisation """

	if __name__ == "__main__":

		root = Tk()
		root.title("View Statistics")
		app = View_Stats(root)
		
		#*** Get the screen resolution and run the frame in fullscreen. ***
		#width, height = root.winfo_screenwidth(), root.winfo_screenheight()
		#root.geometry('%dx%d+0+0' % (width,height))

		root.mainloop()

#--------------------------------------------------------------------------------------------------------------


#*** Main Program ***
main()