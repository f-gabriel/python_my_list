import sys

sys.path.append('c:\\Users\\nilss\\OneDrive\\Skrivbord\\programering\\Python\\Projekt\\my_list\\python_my_list')

from container.container import Container
from place_state.containers_place_state import First_empty_state, Contained_state

class Containers(Container): 
    """#next_item: Container

    def __init__(self, item = None, place_state = First_empty_state):
        #place_state = place_state(self)
        super().__init__(item, place_state)       
        #self.is_before_first_append = is_before_first_append #skapa ett state pattern"""

    def __init__(self, item, place_state = Contained_state, first_container = None):
        state = place_state(self, first_container)
        super().__init__(item, place_state)    
        
    
    """def append(self, item):
        if self.is_before_first_append:
            self.item = item
            self.is_before_first_append = False
        else:
             last_container: Containers = super().__getitem__(len(self)- 1)
             last_container.set_next_item(self.__class__(item, False)) """
        
    def __getitem__(self, index):
        container: Container = super().__getitem__(index)
        return container.get_item()
    
    def __setitem__(self, index, item):
        container: Container = super().__getitem__(index)
        container.set_item(item)

    def __add__(self, items):
        type_self = type(self)
        type_items = type(items)
        if type_items is not type_self:
            raise TypeError(f'can only concatenate {str(type_self)} (not "{str(type_items)}") to {str(type_self)}')
        
        new_containers = Containers()
        item: Containers
        for item in self:
            new_containers.append(item.item)
        for item in items:
            new_containers.append(item.item)   
        return new_containers
        
    def __repr__(self):
        representation = ''
        for item in self:
            representation += str(item.item) + ', '    
        representation = representation[:-2]
        return '(' + representation + ')'
    
    def __iter__(self):
        self.index_place = self
        return self

    """def __next__(self):
        if self.is_before_first_append:
            raise StopIteration
        elif self.iteration_item == None:
            self.iteration_item = self
            raise StopIteration
        else:
            item = self.iteration_item
            self.iteration_item = self.iteration_item.next_item
            return item"""
    
    def __contains__(self, item):
        container: Containers
        for container in self:
            if container.get_item() == item:
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