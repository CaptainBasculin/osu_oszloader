#How does this work?

#Put your /osu/songs folder and  Downloads foler to the creds.json file
#within the same folder of this file like this:
'''
{
"songs" : "/home/user/Games/osu/drive_c/osu/Songs",
"source" : "/home/user/Downloads"
}

'''
#Hit prefill button and start.
#

import getpass
import os
import tkinter as wm
import shutil
import time
from tkinter import messagebox
import json

username = getpass.getuser()

creds = open('creds.json',)
data = json.load(creds)
creds.close()
#This is a GUI version of osuimport.py.
top = wm.Tk()
top.geometry("455x200")
top.title('OSZLoader')

eres = wm.Label(top, bd=5, width = 24)
eres.place(x=10, y=20)
eres["text"]= "/osu!/Songs folder"
e1 = wm.Entry(top, bd=5, width=24)

#TODO: Create a prefill automatically like this format
#prefilltext: Linux-> /home/(username)/Games/osu/drive_c/osu/Songs
#e1["text"]="/home/"+username+"/Games/osu/drive_c/osu/Songs"
e1.place(x=10, y=50)

eree = wm.Label(top, bd=5, width = 24)
eree.place(x=10, y=80)
eree["text"]="Downloads Folder"
e2 = wm.Entry(top, bd=5, width=24)
#e2["text"]="/home/"+username+"/downloads"
e2.place(x=10, y=110)

eshow = wm.Label(top, bd=5, width = 24)
eshow.place(x=234, y=30)
eshow["text"]="No imports yet"

state=False
#0:Stopped, 1: Running
#imp_cter=0

def osuimport(state):
	print("Button pressed!")
	sancheck=True
	state = not state
	print("SET: Songs folder is " + e1.get())
	if not os.path.isdir(e1.get()):
		messagebox.showwarning(title="Bad Input", message="Songs folder invalid!")
		sancheck=False
	print("SET: Downloads folder is " + e2.get())
	if not os.path.isdir(e2.get()):
		messagebox.showwarning(title="Bad Input", message="Downloads folder invalid!")
		sancheck=False
	if(e2.get() == e1.get()):
		messagebox.showwarning(title="Bad Input", message="Both inputs are same!")
		sancheck=False
	if sancheck:
		if(not state):
			loopit=False
			mbutton["text"]="Run"
		else:
			loopit=True
			mbutton["text"]="Stop"
		while(loopit):
			#Put the main logic here
			conts = os.listdir(e2.get())
			check=0
			for i in conts:
				if(i.endswith(".osz")):
					place = e2.get() + "/" + i
					#This should fix the problem for Firefox
					d_time=0
					while(os.stat(place).st_size < 727):
						#Note to self: time.sleep makes the button stuck.
						#Find something that doesn't get the button stuck!
						time.sleep(1)
						d_time=d_time+1
						print("File's being downloaded for " + str(d_time) + " seconds")
				
					''' #Fix for a certain browser 
					downCheck=os.path.getmtime(place) 
					time.sleep(3)
					d_time=3
					while(os.path.getmtime(place)!=downCheck):
						downCheck=os.path.getmtime(place)
						d_time=d_time+1
						print(" File's being downloaded for " + str(d_time) + "seconds")
					time.sleep(1)
					'''
					print("We've moved " + i)
					check=check+1
					shutil.move(place, e1.get())
			if(check==0):
				print("No files moved")
			else:
				print(str(check) + " file(s) moved")
				#imp_cter= imp_cter+1
				#eshow["text"]=(" Total: " + str(imp_cter)+ " Imports")
			time.sleep(5)

def set_text(anan, owo):
	#This sets text for entry objects (anan is entry)
	anan.delete(0,wm.END)
	anan.insert(0,owo)


def pfill():
	#This is a debug code. 
	'''
	set_text(e1, "test2")
	set_text(e2, "test")
	'''
	#Below should be the actual code that reads from a json file
	set_text(e1,data["songs"])
	set_text(e2,data["source"])
	


prefill=wm.Button(top,text="Prefill",command=lambda: pfill())
prefill.place(x=120, y=150)

mbutton=wm.Button(top,text="Run",command=lambda: osuimport(state))
mbutton.place(x=40, y=150)


top.mainloop()


