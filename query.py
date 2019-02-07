
class Query:

    # Make a new query given
    # @param name the start of the filename
    # @param tags The tags of a desired entry
    # @param key the category to sort by
    def __init__(self, name, tags, key=None):

        self.name = name
        self.tags = tags
        self.key = key

    # Given a particular Entry, checks if the entry matches the query
    def matches_query(self, entry):

        # Check if name matches
        if not entry.get_entry_name().startswith(self.name):
            return False

        # Check if tags match

        # For each tag category in the query
        for category in self.tags:

            try:

                # For each tag associated with the category
                for tag in self.tags[category]:

                    # If the tag isn't in the entry, this entry is not a match
                    if tag not in entry.tagsinfo[category]:
                        return False

            except KeyError:

                # If the entry doesn't have data for this category,
                #  it is not a match
                return False

        return True

    # Get all the elements in entry_list that match the query
    def get_entries(self, entry_list):

        matching_entries = []

        for entry in entry_list:

            if self.matches_query(entry):

                matching_entries.append(entry)

        if self.key != None:

            # Sort by the provided category
            matching_entries.sort(key = (lambda x: x.taginfo[self.key]))

        else:

            # Sort by the entry file's name
            matching_entries.sort(key = (lambda x: x.get_entry_name().upper()))
        
        return matching_entries