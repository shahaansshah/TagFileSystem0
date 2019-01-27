#import json


class tagVal:

    #Creates a tag object with a category and entry
    def __init__(self, cat, val):

        self.cat = cat
        self.entry = entry


    #Add a tag to a file
    #read JSON files and create Tag objects from existing files
    #

        #Something about manipulating a JSON file - adding self.entry into the list of the cat json file

    #Store the tag entry in its category's list. So I'm thinking there should be a set of files, each being a tag
    #category, and each category file having a list of entries.




    #My understanding: __repr__ is called when we do something like "print" - by defining __repr__ our way, we can
    #specify what exactly we want to be displayed when we call print?
    def __repr__(self):
        return(self.entry, self.cat)


    #viewtags

