import os
import sys
import subprocess
from JSONlib import *

class Entry:

    # On startup: looks through the JSON files in the "P&R" directory
    # The first thing in the JSON file is a key:value pair of
    # a filepath:entryname. Some loop, perhaps in main.py, checks whether
    # there actually exists an entry 'entryname' in the location
    # 'filepath'.
    #
    # If so, it creates one of these Entry objects, with the tag
    # associations being pulled from the other info in that JSON.

    def __init__(self,json_path):    #inits a file name and path "uniqueID". filepath and entryname are passed in from main or wherever

        self.json_path = json_path
        self.entry_path = readfromJSON(json_path)["Filepath"]

        #How about self.ID=[filepath,entryname] ?
        self.tagsinfo=getTagsfromJSON(json_path) #pulls the tags info from the JSON file to store in tags

    def createNewTag(self,tagval,tagcat): #these need to be input as strings!
        if tagcat in self.tagsinfo:
            self.tagsinfo[tagcat].append(tagval)
        else:
            self.tagsinfo[tagcat] = [tagval]
        newinfo = self.tagsinfo
        newinfo['Filepath'] = self.json_path
        writetoJSON(self.json_path,newinfo)


    def get_json_name(self):
        return os.path.split(self.json_path)[1]

    # Opens the file for viewing
    def open_entry(self):
        if sys.platform.startswith("win32"):
            os.startfile(self.entry_path)
        elif sys.platform.startswith("darwin"):
            subprocess.call(("open", self.entry_path))
        elif sys.platform.startswith("linux"):
            subprocess.call(("xdg-open", self.entry_path))
        else:
            raise NotImplementedError("Not properly implemented for " + sys.platform)


        #Below line --> all wrong!
        #self.tagsinfo = self.tags.append(tagcat:[tagval]) #Create a new entry in tagsinfo - The types going on here are all wrong though
        #writetoJSON(filepath,entryname,data) #How can I append or add to the file?


# path = 'C:\\Users\\Shahaan\\Documents\\DeltahacksPR\\jsonfiletemplate.json'
# newEntry = Entry(path)
# print(newEntry.tagsinfo)
# newEntry.createNewTag(str(input('tag value: ')), str(input('tag category: ')))
# print(newEntry.tagsinfo)