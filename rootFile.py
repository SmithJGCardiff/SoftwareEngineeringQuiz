from tkinter import *
import tkinter.messagebox as tkm
import tkinter.filedialog as tkf
from lib import *
import random
import startPage

# run login window with first argument being startPage as master
root = Tk()
root.title("The Quiz")
root.configure(background = "white")
startPg = startPage.startPage(root)
print(startPg)
root.mainloop()