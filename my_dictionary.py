from containers import Containers
from container import Container
from dictionary_container import *


class My_Dictionary(Containers):

    
    def __init__(self, item = None ,is_before_first_append = True):
        super().__init__(item = None, is_before_first_append = is_before_first_append)
        self.item: Key_Value 
        print('in constructor') 
        print(item)
        """print('self:')
        print(self)"""

    def append(self, key, value = None):
        
        if key in self:
            raise KeyError(f'Key {key} is already in dictionary. Try ____')
        item = Key_Value(key, value)
        print(item)
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

    def __repr__(self):
        item: Key_Value
        representation = ''
        for item in self:
            
            """key = str(item.get_key())
            value = str(item.get_value())
            key_value_string = f'{key}: {value}'"""
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
                item.set_value(value)
                return
        self.append(key, value)


def main():
    d = My_Dictionary()
    #print(d)
    d.append('key_1', 'value_1')
    #print(d)
    d.append('key_2', 'value_2')
    #print(d)
    #print(f'd[key_1] = {d['key_1']}')
    #print(f'd = {d}')
    d['key_1'] = 'value_1'
    #print(f'd = {d}')
    d.append('key_2')




if __name__ == '__main__':
    main()