from multicontainer import Multicontainer

class MyDictionary(Multicontainer):
    def __init__(self, key = None, value=None):
        super().__init__(value, "{}")
        self.key = key

    def add(self, key, value = None):
        key_is_new_key = True
        item: MyDictionary
        for item in self:
            key_is_new_key = key_is_new_key and item.key != key
        if key_is_new_key:
            last_dictionary_pos = self[len(self -1)]
