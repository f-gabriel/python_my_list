from containers import Containers
from container import Container
from value import Value

class My_Dictionary(Containers):
    def __init__(self, is_first_append = True):
        super().__init__(None, is_first_append)


    def append(self, key, value = None):
        item = Container(key)
        item.append(value)
        super().append(item)
    
    def items(self):
        items = Containers()
        for item in self:
            items.append(item)
        return items
    
    

    def __getitem__(self, key):
        item: My_Dictionary
        for item in self:
            if self.key == key:
                return item.get_value()   
        raise KeyError  

    def __contains__(self, item):
        container: My_Dictionary
        for container in self:
            if container.key == item:
                return True
        return False

    def __setitem__(self, key, value):
        if key in self:
            self      
