from abc import ABC, abstractmethod

class C_Implementation_Interface(ABC):
    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def add_owner(self, owner):
        pass

class C_Implementation(C_Implementation_Interface): 
    owner: object

    def __init__(self, owner = None):
        super().__init__()
        self.owner = owner
    
    def append(self, item):
        match None:
            case self.owner.value: 
                self.owner.value = item
                return
            case self.owner.next_value: 
                self.owner.next_value = item
                return
            case _: raise IndexError
    def add_owner(self, owner):
        self.owner = owner

class Main_C_Implementation(C_Implementation):
    def append(self, item):
        new_item = self.owner.__class__(item, Regular_C_Implementation)
        try: 
            super().append(new_item)
        except IndexError:
            self.owner.next_value.append(new_item)

class Regular_C_Implementation(C_Implementation):
    def append(self, item):
        try: 
            super().append(item)
        except IndexError:
            self.owner.next_value.append(item)