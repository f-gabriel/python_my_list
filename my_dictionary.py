from multicontainer import Multicontainer
from new_implimentation.value import Value

class MyDictionary(Multicontainer):
    key = Value()
    
    def __init__(self, key = None, value=None):
        super().__init__(value, "{}")
        self.key = key

    def add(self, key, value = None):
        key_is_new_key = True
        item: MyDictionary
        for item in self:
            key_is_new_key = key_is_new_key and item.key != key
        if key_is_new_key:
            self.add(value)
            new_container: MyDictionary = self[len(self) -1]
            new_container.key = key

    def items():


    def __getitem__(self, key):
        item: MyDictionary
        for item in self:
            if self.key == key:
                return item.get_value()   
        raise KeyError  

    def __contains__(self, item):
        container: MyDictionary
        for container in self:
            if container.key == item:
                return True
        return False

    def __setitem__(self, key, value):
        if key in self:
            self      
