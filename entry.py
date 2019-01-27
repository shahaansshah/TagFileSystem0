import os
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

    def __init__(self,fullpath):    #inits a file name and path "uniqueID". filepath and entryname are passed in from main or wherever

        #How about self.ID=[filepath,entryname] ?
        self.fullpath = fullpath
        (self.directory, self.name) = os.path.split(fullpath)
        self.tagsinfo=getTagsfromJSON(fullpath) #pulls the tags info from the JSON file to store in tags

    def createNewTag(self,tagval,tagcat):
        #Below line --> all wrong!
        #self.tagsinfo = self.tags.append(tagcat:[tagval]) #Create a new entry in tagsinfo - The types going on here are all wrong though
        #writetoJSON(filepath,entryname,data) #How can I append or add to the file?
        pass

    def __repr__(self):
        return (self.name + " in " + self.directory)
# path = 'C:\\Users\\Shahaan\\Documents\\DeltahacksPR\\jsonfiletemplate.json'
# newEntry = Entry(path)
# print(newEntry.tagsinfo)
