from container import *

class Containers(Container): 
    next_value: Container

    def __init__(self, value = None, is_first_append = True):
        super().__init__(value)        
        self.is_first_append = is_first_append
    
    def append(self, item):
        if self.is_first_append:
            self.value = item
            self.is_first_append = False
        else:
             last_container: Containers = super().__getitem__(len(self)- 1)
             last_container.set_next_value(self.__class__(item, False))
        
    def __getitem__(self, index):
        return super().__getitem__(index).get_value()
    
    def __setitem__(self, index, value):
        super().__getitem__(index).set_value(value)

    def __add__(self, items):
        type_self = type(self)
        type_items = type(items)
        if type_items is not type_self:
            raise TypeError(f'can only concatenate {str(type_self)} (not "{str(type_items)}") to {str(type_self)}')
        
        new_containers = Containers()
        item: Containers
        for item in self:
            new_containers.append(item.value)
        for item in items:
            new_containers.append(item.value)   
        return new_containers
        
    def __repr__(self):
        representation = ''
        for value in self:
            representation += str(value.value) + ', '    
        representation = representation[:-2]
        return '(' + representation + ')'
    
    def __iter__(self):
        self.iteration_value = self
        return self

    def __next__(self):
        if self.is_first_append:
            raise StopIteration
        elif self.iteration_value == None:
            self.iteration_value = self
            raise StopIteration
        else:
            item = self.iteration_value
            self.iteration_value = self.iteration_value.next_value
            return item
    
    def __contains__(self, item):
        container: Containers
        for container in self:
            if container.get_value() == item:
                return True
        return False
    
    def __len__(self): 
        length = 0
        for _ in self:
            length += 1
        return length 
        
        
    

def main():
    a = Containers()
    b = Containers()
    for i in range(3):
        a.append(i)
    for i in range(3):
        b.append(i + 3)
    a.append(None)
    c = a + b
    print(c)
        
    
    

if __name__ == '__main__':
    main()