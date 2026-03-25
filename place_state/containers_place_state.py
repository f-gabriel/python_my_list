import sys

sys.path.append('c:\\Users\\nilss\\OneDrive\\Skrivbord\\programering\\Python\\Projekt\\my_list\\python_my_list')

import place_state
#from place_state.place_state import Place_state
from container.contains_interface import I_Contains


class First_empty_state(Place_state):
    def append(self, item):
        self.owner.set_item(item) 
        self.owner.set_state(First_last_state(self.owner))

    def __next__(self):
        raise StopIteration
    
class First_last_state(Place_state):
    def append(self, item):
        owner_type_obj = self.owner.__class__(self.owner, item, Last_place_state)
        self.owner.set_next_item(owner_type_obj) 
        self.owner.set_state(First_middle_state(self.owner))

    def __next__(self):
        if self.owner.get_index_place_keeper() is self.owner: 
            self.owner.set_index_place_keeper(None)
            return self.owner.get_item()   
        return StopIteration
    
class First_middle_state(Place_state):
    def append(self, item):
        next_container: I_Contains = self.owner.get_next_item()
        next_container.append(item)

    def __next__(self):
        next_container: I_Contains = self.owner.get_next_item()
        self.owner.set_index_place_keeper(next_container)
        return self.owner




class Contained_state(Place_state):
    first_container: I_Contains 

    def __init__(self, owner, first_container = None):
        super().__init__(owner)
        self.first_container = first_container

    def set_first_container(self, first_container:I_Contains):
        self.first_container = first_container


class Last_place_state(Contained_state):
    def append(self, item):
        owner_type_obj = self.owner.__class__(self.first_container, item, Last_place_state)
        self.owner.set_next_item(owner_type_obj) 
        self.owner.set_state(Middle_place_state(self.owner, self.first_container))

    def __next__(self):
        if self.first_container.get_index_place_keeper() == None:
            raise StopIteration
        self.first_container.set_index_place_keeper(None)
        return self.owner
    

class Middle_place_state(Contained_state):
    def append(self, item):
        next_container: I_Contains = self.owner.get_next_item()
        next_container.append(item)

    def __next__(self):
        next_container: I_Contains = self.owner.get_next_item()
        self.first_container.set_index_place_keeper(next_container)
        return self.owner