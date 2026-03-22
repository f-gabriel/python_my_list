from new_container import *
from container_implementation import *

class Containers(New_Container): 
    implementation: C_Implementation_Interface
    next_value: New_Container
    

    def __init__(self, value = None, implementation = Main_C_Implementation):
        super().__init__(value)
        self.implementation = implementation(self)        
    
    def append(self, item):
        print(len(self))
        if len(self) == 0:
            print('is in append if')
            self.value = item
        else:
             last_container: Containers = super().__getitem__(len(self)- 1)
             last_container.set_next_value(self.__class__(item, Regular_C_Implementation))
        """self.implementation.append(item)"""

    def __getitem__(self, index):
        return super().__getitem__(index).get_value()
    
    def __setitem__(self, index, value):
        super().__getitem__(index).set_value(value)

    def __add__(self, items):
        type_self = type(self)
        type_items = type(items)
        if type_items is type_self:
            item: Containers
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
            print('is in if')
            self.iteration_value = self
            raise StopIteration
        else:
            print('is in else')
            item = self.iteration_value
            self.iteration_value = self.iteration_value.next_value
            return item
    
    def __contains__(self, item):
        container: Containers
        for container in self:
            if container.get_value() == item:
                return True
        return False
    
    def __len__(self): # funkar inte som den ska
        length = -1
        for _ in self:
            print('is in len')
            length += 1
        #if length <= 0: return 0
        return length 
        
        
    

def main():
    a = Containers()
    a.append(3)
    print(a)
    print(len(a))

    """a.append('strumpa')
    for i in range(4):
        a.append(i)

    b = Containers()
    b.append(6)
    b.append(None)
    b.append(7)

    a.append(b)
    a + b

    #print(f'len is {len(a)}')
    #print(f'a[4] is {a[4]}')
    #print(f'a[-3] is {a[-3]}')
    #print(f'a is {a}') 
    a[-3] = None
    #print(f'a is after a[-3] change {a}')
    #print(f'string of None is {str(None)}')
    a.append(None)
    #print(f'len is {len(a)}')"""
    
    

if __name__ == '__main__':
    main()