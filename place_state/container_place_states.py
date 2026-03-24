from place_state.place_state import Place_state


class Container_empty_state(Place_state):
    def append(self, item):
        self.owner.set_item(item) 
        self.owner.set_state(Container_open_state(self.owner))

    def __next__(self):
        raise StopIteration
    
class Container_open_state(Place_state):
    def append(self, item):
        self.owner.set_next_item(item)
        self.owner.set_state(Container_closed_state(self.owner))

    def __next__(self):
        if self.owner.get_index_place_keeper() == 0:
            
            self.owner.set_index_place_keeper(1)
            return self.owner.get_item()
        raise StopIteration
    
class Container_closed_state(Place_state):
    def append(self, item):
        raise IndexError('Container can only hold 2 items')
    
    def __next__(self):
        if self.owner.get_index_place_keeper() == 0:
            self.owner.set_index_place_keeper(1)
            print(f'first next {self.owner.get_item()}')
            return self.owner.get_item()
        elif self.owner.get_index_place_keeper() == 1:
            self.owner.set_index_place_keeper(2)
            return self.owner.get_next_item()
        else:
            self.owner.set_index_place_keeper(0)
            raise StopIteration

