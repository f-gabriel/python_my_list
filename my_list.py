from multicontainer import Multicontainer
from container import *


class My_List(Multicontainer):
    def __init__(self, value = None):
        super().__init__(value, '[]')
            
    def get_values(self):
        next: My_List = super().__next__()
        return next.get_value()
    
    def __add__(self, other: My_List):
        item: My_List
        for item in other:
            self.add(item.get_value())
        return self

    def __getitem__(self, key):
        item: My_List = super().__getitem__(key)
        return item.get_value()
        
    
    def sort():
        pass