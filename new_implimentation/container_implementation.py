from abc import ABC, abstractmethod
from contains_interface import I_Contains

class C_Implementation_Interface(ABC):
    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def add_owner(self, owner):
        pass



class C_Implementation(C_Implementation_Interface): 
    owner: I_Contains

    def __init__(self, owner = None):
        super().__init__()
        self.owner = owner
    
    def append(self, item):
        if self.owner.get_value() == None: 
            self.owner.set_value(item)
            return
        elif self.owner.get_next_value() == None: 
            self.owner.set_next_value(item)
            return
        else: 
            raise IndexError 

    def add_owner(self, owner):
        self.owner = owner



class Main_C_Implementation(C_Implementation):
    def append(self, item):
        if self.owner.get_value() == None:
            self.owner.set_value(item)
            return
        new_item = self.owner.__class__(item, Regular_C_Implementation)
        try: 
            super().append(new_item)
            return
        except IndexError:
            self.owner.get_next_value().append(new_item)



class Regular_C_Implementation(C_Implementation):
    def append(self, item):
        try: 
            super().append(item)
            return
        except IndexError:
            self.owner.get_next_value().append(item)