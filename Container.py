from container_helpers import *
from new_implimentation.value import Value
from abc import ABC, abstractmethod

        

class Container(ABC):
    value = Value()
    next_value = Value()

    def __init__(self, value = None):
        self.value = value
        self.next_value = None
        
    @abstractmethod
    def add(self, item):
        pass
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def get_next_value(self):
        return self.next_value
    
    def set_next_value(self, value):
        self.next_value = value
    
    
    
        


        


     