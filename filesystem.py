
import os

JSON_DATA_FOLDER = "PR_DATA"

from entry import Entry

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

        # Create and add any missing files
        #for item in 


        # Check if the filestructure matches the 
        # current

    # Used when the program is starting up in order to create new
    #  metadata files for all contained files
    def setup(self, folder=None):
        
        # Get a listing of all the files and directories in this directory
        #  If we are on the recursive call, use the passed folder name
        #  Otherwise, use the directory of the filesystem
        dir_listing = os.listdir(folder if folder!=None else self.directory)

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

    fs = FileSystem("C:\\Users\\david\\Documents\\Programming\\DeltaHacksV\\TagFileSystem0")

    print(fs)

    pass


# TODO: comment out
main()