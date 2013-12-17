#!usr/local/bin/python3.3
'''Loading python3 also loads 3.3 if it is available, so just load 3.3 (or 3.3.3)'''

'''Getting the module'''
import os
import sys
import re
import subprocess
from os import listdir
from os.path import isfile, join

fileLst = []
dictLink = {}
lenArgv = len(sys.argv)

'''Checking the argument on the command line'''
if lenArgv == 1:
    sys.exit("TraceLink.py Synopsis:\npython3.3 tracelink.py [dir]\npython3.3 tracelink.py [opition] [dir]\n\nCommand line option:\n-r, recursion is enable.\n")

elif 2 <= lenArgv <= 3:
    if sys.argv[1] == '-r': #check for recursion option
        if lenArgv < 3: #If there is a path
            sys.exit("Path of directory was not provide.")

        elif os.path.isdir(sys.argv[2]): #check if it is a directory
            directory = os.path.abspath(sys.argv[2]) #change path to full path
            for dirName, subdirlist, fileName in os.walk(directory): #Walking through the directory and store full path
                for name in fileName:
                    lst= dirName + "/" + name
                    fileLst.append(lst)

    elif os.path.isdir(sys.argv[1]):
        directory = os.path.abspath(sys.argv[1])
        for fileName in listdir(directory): #Find all the file at current directory
            tmpPath = join(directory,fileName)  #add the filename to the full path
            if isfile(tmpPath):
                fileLst.append(tmpPath)
    else:
        sys.exit("Invalid formatting")

if len(fileLst) == 0:   #Empty list terminate the program
        sys.exit("Current path have no files")

# Extract distinct (unique) download history locations via the terminal
downloadHistory = os.popen("sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select distinct LSQuarantineDataURLString from LSQuarantineEvent'").read()

for fname in fileLst:       
    #Use mdls and grep for the url
    proc1 = subprocess.Popen(["mdls", fname], stdout =subprocess.PIPE)
    proc2 = subprocess.Popen(["grep", "http"], stdin=proc1.stdout, stdout=subprocess.PIPE)
    url = str(proc2.communicate()[0])

    if url == "b\'\'": #if there is no url
        dictLink[fname] = "Can't determine the source of the website"
    else:
        link = url.split("\"")[1]
        histList = downloadHistory.split("\n")
        for dlink in histList:
                if link == dlink:
                        file = open('Output.txt', 'a')
                        file.write("The file " + fname + " was found on this system with the download link " + link + " and was downloaded on this system.\n")
						file.close()
						
