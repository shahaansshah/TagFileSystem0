


# Represents a bunch of tagges files
class FileSystem:

    # Make a filesystem given a particular directory
    def __init__(self, directory):

        # All the files in the system
        self.files = []

        self.directory = directory

        # TODO:

        # Check for existing group of tags for files

        # Read the filestructure

        # Check if the filestructure matches the 
        # current 

    # Given a file change, solve the file chagne in the metadata about the files
    def resolve_delta(self, delta):

        # TODO:

        pass

    # Get a subset of the files using a query
    def query_files(self, query):

        # TODO:

        matching = []

        for file in self.files:

            if query.check_matches(file):

                matching.append(file)

        return matching
