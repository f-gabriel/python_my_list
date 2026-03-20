from container import *
from container_helpers import *
from container_interfaces import I_Has_Iterator as IHI

class Multicontainer(Container, IHI):
    def __init__(self, value = None, brackets = ''):
        super().__init__(value)
        self.iterator = Container_Itterator(self) # keeps track of next item to return in __next__() and similar functions
        self.representation = String_Representation(self, brackets)

    def add(self, item):
        if self.value == None:
            self.value = item
            return
        elif self.next_value == None:
            self.next_value = self.__class__()
        self.next_value.add(item)
            
    def __len__(self):
        length = 0
        for item in self:
            length += 1
        return length
    
    def __set__(self, instance, value):
        container: Multicontainer = self.__get__(instance)
        container.set_value(value)
        

    def __getitem__(self, key):
        index = 0
        item: Container
        for item in self:
            if index == key:
                return item
            index += 1
        raise IndexError

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return self.iterator.__next__()
        except StopIteration:
            raise    
        
    def __repr__(self):
        return self.representation.string_representation()
        