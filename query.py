
class Query:

    # Make a new query given what the filename starts with
    #  as well as the list of tags that need to me matched
    def __init__(self, name, tags):

        self.name = name
        self.tags = tags

    # Given a particular file object, checks if the file
    #  matches the query
    def check_matching(self, file):

        # TODO:

        # Check that the first characters of the file name 
        #  match

        # Check that all the tags in this query are in the file

        return True