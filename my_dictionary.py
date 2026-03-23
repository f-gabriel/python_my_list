from containers import Containers
from container import Container
from value import Value

class My_Dictionary(Containers):
    def __init__(self, is_first_append = True):
        super().__init__(None, is_first_append)


    def append(self, key, value = None):
        if key in self:
            self[key] = value
        item = Container(key)
        item.append(value)
        super().append(item)
    
    def items(self): # inte klar
        items = Containers()
        for item in self:
            items.append(item)
        return items
    
    def get_key(self):
        return self.value.value
    
    def get_item_value(self):
        return self.value.next_value
    
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
                return item.get_item_value()   
        raise KeyError  

    def __contains__(self, item):
        container: My_Dictionary
        for container in self:
            if container.key == item:
                return True
        return False

    def __setitem__(self, key, value):
        item: My_Dictionary
        for item in self:
            if self.get_key() == key:

