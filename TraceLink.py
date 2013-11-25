#!usr/bin/python3.3

'''Getting the module'''
import os
import sys
import subprocess
from os import listdir
from os.path import isfile, join


check = 0
fileLst = []

while(check != 1):
    directory = input("Enter the full (absolute) path of the directory: ")
    if os.path.isdir(directory):    #check if directory exists
        recur = input("Would you like to recursively look through the path? (y) (n): ")
        if recur == "y":
            check = 1
            for dirName, subdirlist, fileName in os.walk(directory): #Walking through the directory and store full path
                for name in fileName:
                    fileLst = dirName + "/" + name
        elif recur == "n":
            check = 1
            for fileName in listdir(directory): #Find all the file at current directory
                tmpPath = join(directory,fileName)  #add the filename to the full path
                if isfile(tmpPath):
                    fileLst.append(tmpPath)
        else:
            print("Not a valid option")
    else:
        print("Not a valid path")

if len(fileLst) == 0:   #Empty list terminate the program
	sys.exit("Current path have no files")
	
for file in fileLst:
    '''
    Going through arrary do a mdls check 
    Prase the mdls to get only the webiste where it was download
    Create a two dictionary: 
    1. filename ---> link
    2. filename ---> no link 
    '''
    proc = subprocess.Popen(["mdls", file], stdout=subprocess.PIPE)
    out = str(proc.communicate()[0])
    nWord = out.lstrip("b\'")
    #Parse string to remove \n and look for web link
    
# Extract distinct (unique) download history locations via the terminal
downloadHistory = os.system("sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select distinct LSQuarantineDataURLString from LSQuarantineEvent'")
