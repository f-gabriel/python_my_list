from Multicontainer import Multicontainer as MC
from Container import Container


class My_List(MC):
    def __init__(self, value = None):
        super().__init__(value, '[]')
            
    def get_values(self):
        next: My_List = super().__next__()
        return next.get_value()
    
    def __add__(self, other: MC):
        for item in other:
            self.add(item)

    def __getitem__(self, key):
        item: Container = super().__getitem__(key)

        return item.get_value()

    

    def sort():
        pass