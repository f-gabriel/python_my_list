from Multicontainer import Multicontainer

class MyDictionary(Multicontainer):
    def __init__(self, key, value=None):
        super().__init__(value, "{}")
        self.key = key

    def add(self, key):
        