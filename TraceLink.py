#!/usr/bin/python3.2

'''Getting the module'''
import os
from os import listdir
from os.path import isfile, join

check = 0

while(check != 1):
	directory = input("Enter the full path of the directory: ")
	if os.path.isdir(directory):	#check if directory exist
		recur = input("Would you like to recursively look through the path? (y) (n): ")
		if recur == "y":
			check = 1
			#Recursive fucntion
			#Add each file with the full path to an array/list/hash
			print("yes")
		elif recur == "n":		
			check = 1
			fileLst = []
			for fileName in listdir(directory):	#Find all the file at current directory
				tmpPath = join(directory,fileName)	#add the filename to the full path
				if isfile(tmpPath):
					fileLst.append(tmpPath)	

			if len(fileLst) == 0:
				print ("Current path have no files")
			else:
				for validFile in fileLst:
					os.system("mdls " + validFile);
		else:
			print("Not a valid option")
	else:
		print("Not a valid path")
		
	
	



