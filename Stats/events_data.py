#*** Imports ***
from tkinter import *
from tkinter import messagebox
import shelve
import sys
import time







def play_time():
	'''Returns the time at which the user played the game.'''	
	
	time.strftime('%X %x %Z')
	game_time = time.asctime(time.localtime(time.time()))
	return game_time[0:11] # Display only Day-Month-Date 
	

print(play_time())