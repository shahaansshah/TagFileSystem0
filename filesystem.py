
import os
from JSONlib import *

JSON_DATA_FOLDER = "PR_DATA"

from entry import Entry

# NOTE: the JSON files are all named numbers because its easier

# Used to get a list of files in a directory
# Basically the tree command
def get_all_file_paths(abs_directory):

    paths = []

    dir_listing = os.listdir(abs_directory)

    # Add all files in this directory
    for item in dir_listing:
        item_full_path = os.path.join(abs_directory, item)
        if os.path.isfile(item_full_path):
            paths.append(item_full_path)
    
    # Recursively go into folders and add files there
    for item in dir_listing:
        item_full_path = os.path.join(abs_directory, item)
        if os.path.isdir(item_full_path):
            paths.extend(get_all_file_paths(item_full_path))

    # Return the list of paths
    return paths


# Represents a bunch of tagged files
class FileSystem:

    # Make a filesystem given a particular directory
    def __init__(self, directory):

        # All the files in the system
        self.entries = []

        self.directory = directory

        # TODO:

        # Check for existing group of tags for files
        
        # https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # get the folder with the JSON files in it
        json_dir = os.path.join(current_dir, JSON_DATA_FOLDER)

        highest = -1

        try:

            # Get the members of the folder
            members_json_folder = os.listdir(path=json_dir)

            # for each of the members
            for item in members_json_folder:

                # contruct the abs path name
                file_abs_path = os.path.join(json_dir, item)

                # Make sure it is a JSON file
                if os.path.isfile(file_abs_path) and item.endswith(".json"):

                    curr_entry = Entry(file_abs_path)

                    if curr_entry == None:
                        # If the entry is not there, remove the JSON
                        os.remove(file_abs_path)
                    else:
                        # Add it to the entries list
                        self.entries.append(curr_entry)

            # sort entries my name in ascending numerical order
            self.entries.sort(key=(lambda x: int(x.get_json_name()[0:-5])))

            # Get the highest numbered JSON file
            highest = int(self.entries[-1].get_json_name()[0:-5])

        except FileNotFoundError:
            os.mkdir(json_dir, 0o777)

        # Create and add any missing JSON files
        all_paths = get_all_file_paths(directory)

        for item in all_paths:
            found = False
            for entry in self.entries:
                if entry.entry_path == item:
                    found = True
                    break
            if found:
                continue
            # Otherwise, we need to make a JSON for it
            writetoJSON(os.path.join(json_dir, str(highest+1) + ".json"),
                        {"Filepath":item})
            highest += 1
            


        # Check if the filestructure matches the 
        # current

    # Used when the program is starting up in order to create new
    #  metadata files for all contained files
    def setup(self, folder=None):
        
        # Get a listing of all the files and directories in this directory
        #  If we are on the recursive call, use the passed folder name
        #  Otherwise, use the directory of the filesystem
        dir_listing = os.listdir(folder if folder != None else self.directory)

        for item in dir_listing:
            if os.path.isfile(item):
                self.entries.append(Entry(item))

        pass


    # Given a file change, solve the file changed in the metadata about the files
    #  Used when the program is running
    def resolve_delta(self, delta):

        # TODO:

        pass

    # Get a subset of the files using a query
    def query_files(self, query):

        # TODO:

        matching = []

        for file in self.entries:

            if query.check_matches(file):

                matching.append(file)

        return matching

    def __repr__(self):
        
        string_rep = ""

        for entry in self.entries:
            string_rep += str(entry) + "\n"

        return string_rep

# Unit testing

def main():

    fs = FileSystem("/home/david/Documents/DankerMemes")

    pass


# TODO: comment out
main()