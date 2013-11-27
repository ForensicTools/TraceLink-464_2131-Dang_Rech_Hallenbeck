#!usr/bin/python3.3

'''Getting the module'''
import os
import sys
import re
import subprocess
from os import listdir
from os.path import isfile, join


check = 0
fileLst = []
dictLink = {}

while(check != 1):
    directory = input("Enter the full (absolute) path of the directory: ")
    if os.path.isdir(directory):    #check if directory exists
        recur = input("Would you like to recursively look through the path? (y) (n): ")
        if recur == "y":
            check = 1
            for dirName, subdirlist, fileName in os.walk(directory): #Walking through the directory and store full path
                for name in fileName:
                    lst= dirName + "/" + name
                    fileLst.append(lst)
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

for fname in fileLst:		
    #Use mdls and grep for the url
    proc1 = subprocess.Popen(["mdls", fname], stdout =subprocess.PIPE)
    proc2 = subprocess.Popen(["grep", "http"], stdin=proc1.stdout, stdout=subprocess.PIPE)
    url = str(proc2.communicate()[0])

    if url == "b\'\'": #if there is no url
	    dictLink[fname] = "Can't determine the source of the website"
    else:
	    match = re.findall('(https?://[^\s"]+)', url) #regex for http/https link
	    dictLink[fname] = match

# Extract distinct (unique) download history locations via the terminal
downloadHistory = os.system("sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select distinct LSQuarantineDataURLString from LSQuarantineEvent'")
