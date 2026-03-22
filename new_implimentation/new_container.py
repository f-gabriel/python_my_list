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

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
            #print(f'index is {index}')
        if index > len(self):
            raise IndexError
        
        counter = 0
        for item in self:
            if counter == index:
                return item
            counter += 1

    def __setitem__(self, index, value):
        match index:
            case 0: 
                return self.set_value(value)
            case 1: 
                return self.set_next_value(value)
            case _: 
                raise IndexError

    def __add__(self, item):
        self.append(item)

    def __repr__(self):
        representation = ''
        for value in self:
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
    
    def __len__(self):
        return 2
        


def main():
    a = New_Container()
    print(len(a))
    a + 1
    a + 2
    print(a[0])
    print(a[1])
    a[1] = 5

    print(a)
    #a + 3

if __name__ == '__main__':
    main()