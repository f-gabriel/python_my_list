from value import Value
from abc import ABC, abstractmethod
from container_implementation import *

class New_Container(ABC):
    value = Value()
    next_value = Value()
    implementation: C_Implementation_Interface

    def __init__(self, value = None):
        self.value = value
        self.next_value = None
        self.implementation = C_Implementation(self)
        
    def __add__(self, item):
        self.append(item)
    
    def set_value(self, item):
        self.value = item

    def __len__(self):
        length = 0
        for item in self:
            if self != None:
                length += 1
        return length

    def append(self, item):
        self.implementation.append(item)
        #match None:
        #    case self.value: 
        #        self.value = item
        #        return
        #    case self.next_value: 
        #        self.next_value = item
        #        return
        #    case _: raise IndexError

    def __repr__(self):
        representation = ''
        for value in self:
            if value != None:
                representation += str(value) + ', '    
        representation = representation[:-2]
        return representation
    
    def __iter__(self):
        self.test_index = 0  # For testeing, mainly of __next__. should be removed later
        return self
    
    def __next__(self):
        self.test_index += 1
        match self.test_index:
            case 1: 
                return self.value
            case 2: 
                return self.next_value
            case _: 
                self.test_index = 0
                raise StopIteration
        


def main():
    a = New_Container()
    a + 1
    a + 2
    print(a)

if __name__ == '__main__':
    main()