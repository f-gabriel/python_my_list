from containers import Containers
from container import Container
from dictionary_container import *


class My_Dictionary(Containers):
    def __init__(self, item = None, value = None, is_before_first_append = True):
        if item == None:
            item = item
        elif (type(item) != Key_Value):
            item = Key_Value(item, value)   
        super().__init__(item, is_before_first_append = is_before_first_append)
        self.item: Key_Value 

    def append(self, key, value = None):
        if key in self:
            raise KeyError(f'Key {key} is already in dictionary. Try ____')
        item = Key_Value(key, value)
        super().append(item)
    
    def items(self): # går inte att komma åt key och value på ett smidigt sätt
        items = Containers()
        for item in self:
            items.append(item)
        return items
    
    def get_key(self):
        return self.item.get_key()
    
    def get_value(self):
        return self.item.get_value()
    
    def set_value(self, value):
        print(f'value in setitem is {value}')
        self.item.set_value(value)

    def keys(self):
        keys_containers = Containers() #skapa abstract factory
        for item in self:
            keys_containers.append(item.get_key())
        return keys_containers
            
    def __repr__(self):
        item: Key_Value
        representation = ''
        for item in self:
            representation += str(item.item) + ', '    
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
        for item in self:
            if item.get_key() == key:
                print(f'value in setitem is {value}')
                item.set_value(value)
                return
        self.append(key, value)


def main():
    ...


if __name__ == '__main__':
    main()