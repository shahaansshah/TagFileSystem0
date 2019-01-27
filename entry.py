
import os

class Entry:

    def __init__(self, abs_path):

        self.abs_path = abs_path

        (self.path, self.name) = os.path.split(abs_path)
