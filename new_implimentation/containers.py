from new_container import *
from container_implementation import *

class Containers(New_Container): 
    implementation: C_Implementation_Interface
    next_value: New_Container
    

    def __init__(self, value = None, implementation = Main_C_Implementation):
        super().__init__(value)
        self.implementation = implementation(self)        
    
    def append(self, item):
        self.implementation.append(item)

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError
        counter = 0
        for item in self:
            if counter == index:
                return item
            counter += 1

    def __add__(self, items):
        type_self = type(self)
        type_items = type(items)
        if type_items is type_self:
            for item in items:
                self.append(item.value)
        else:
            raise TypeError(f'can only concatenate {str(type_self)} (not "{str(type_items)}") to {str(type_self)}')
        
    def __repr__(self):
        representation = ''
        for value in self:
            if value != None:
                representation += str(value.value) + ', '    
        representation = representation[:-2]
        return '(' + representation + ')'
    
    def __iter__(self):
        self.iteration_value = self
        return self

    def __next__(self):
        if self.iteration_value == None:
            self.iteration_value = self
            raise StopIteration
        else:
            item = self.iteration_value
            self.iteration_value = self.iteration_value.next_value
            return item
    

def main():
    a = Containers()
    a.append(3)
    a.append('strumpa')
    for i in range(4):
        a.append(i)

    b = Containers()
    b.append(6)
    #b.append(None)
    b.append(7)

    a.append(b)
    a + b

    print(a) 

if __name__ == '__main__':
    main()