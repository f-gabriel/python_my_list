from containers import Containers
from container import Container
from dictionary_container import *


class My_Dictionary(Containers, Dictionary_Interface):
    def __init__(self, is_first_append = True):
        super().__init__(None, is_first_append)
        self.item: Key_Value


    def append(self, key, value = None):
        if key in self:
            raise KeyError(f'Key {key} is already in dictionary. Try ____')
            self[key] = item
        item = Key_Value(key, value)
        super().append(item)
    
    def items(self): # inte klar
        items = Containers()
        for item in self:
            items.append(item)
        return items
    
    def get_key(self):
        return self.item.get_key()
    
    def get_value(self):
        return self.item.get_value()
    
    def __repr__(self):
        representation = ''
        for item in self:
            key = str(item.get_key())
            value = str(item.get_item_value())
            key_value_string = f'{key}: {value}'
            representation += key_value_string + ', '    
        representation = representation[:-2]
        return '{' + representation + '}'

    def __getitem__(self, key):
        item: My_Dictionary
        for item in self:
            if self.get_key() == key:
                return item.get_value()   
        raise KeyError  

    def __contains__(self, key):
        container: My_Dictionary
        for item in self:
            if item.get_key() == key:
                return True
        return False

    def __setitem__(self, key, value):
        item: Key_Value
        if key in self:

        for item in self:
            if self.get_key() == key:
                ...

