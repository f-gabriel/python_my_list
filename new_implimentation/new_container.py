from value import Value
from container_implementation import *
from contains_interface import I_Contains

class New_Container(I_Contains):
    value = Value()
    next_value = Value()
    implementation: C_Implementation_Interface

    def __init__(self, value = None):
        self.value = value
        self.next_value = None
        self.implementation = C_Implementation(self)
        
    def get_value(self):
        return self.value

    def set_value(self, item):
        self.value = item

    def get_next_value(self):
        return self.next_value
    
    def set_next_value(self, item):
        self.next_value = item

    def append(self, item):
        self.implementation.append(item)

    def __add__(self, item):
        self.append(item)

    def __len__(self):
        length = 0
        for item in self:
            if self != None:
                length += 1
        return length

    def __repr__(self):
        representation = ''
        for value in self:
            if value != None:
                representation += str(value) + ', '    
        representation = representation[:-2]
        return representation
    
    def __iter__(self):
        self.test_index = 0 
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
    #a + 3

if __name__ == '__main__':
    main()