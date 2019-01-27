class Entry:

    # On startup: looks through the JSON files in the "P&R" directory
    # The first thing in the JSON file is a key:value pair of
    # a filepath:entryname. the init for this class checks whether
    # there actually exists an entry 'entryname' in the location
    # 'filepath'.
    #
    # If so, it creates one of these Entry objects, with the tag
    # associations being pulled from the other info in that JSON.

    #inits a file name and path "uniqueID"
    def __init__(self):
        
