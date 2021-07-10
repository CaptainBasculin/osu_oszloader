#Plan: Check contents of downloads folder regularly.
#if contains .osu file, carry it to osu folder.

import os
import shutil
import time

songs = "/home/notbaitm8/Games/osu/drive_c/osu/Songs"

source = "/home/notbaitm8/İndirilenler"

#DEBUG
while True:
	conts = os.listdir(source)
	check=0
	for i in conts:
		if(i.endswith(".osz")):
			place = source + "/" + i
			#This should fix the problem for Firefox
			d_time=0
			while(os.stat(place).st_size < 727):
				time.sleep(1)
				d_time=d_time+1
				print(" File's being downloaded for " + str(d_time) + "seconds")
				
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
			shutil.move(place, songs)
	if(check==0):
		print("No files moved")
	else:
		print(str(check) + " file(s) moved")
	time.sleep(5)

