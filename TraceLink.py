usr/bin/python3.2

'''Getting the module'''
import os
from os import listdir
from os.path import isfile, join

# Subprocess doesnt currently work
from subprocess import call

check = 0

while(check != 1):
        directory = input("Enter the full (absolute) path of the directory: ")
        if os.path.isdir(directory):        #check if directory exists
                fileLst = []
                recur = input("Would you like to recursively look through the path? (y) (n): ")
                if recur == "y":
                        check = 1
                        #Recursive function
                        fileLst = os.system('find ' + directory + ' -type f')
                        # fileLst = call("find /root/ -type f") # this currently doesnt work
                        for validFile in fileLst:
                        	# Using file like the below example to test on Linux
                        	os.system("file " + validFile)
                elif recur == "n":
                        check = 1
                        for fileName in listdir(directory):        #Find all the file at current directory
                                tmpPath = join(directory,fileName)        #add the filename to the full path
                                if isfile(tmpPath):
                                        fileLst.append(tmpPath)
                                        
                        if len(fileLst) == 0:
                                print ("Current path have no files")
                        else:   
                                for validFile in fileLst:
                                        os.system("file " + validFile)
                                        # Using the above for testing on Linux, we would be using mdls normally
         else:
                        print("Not a valid option")
        else:
                print("Not a valid path")
