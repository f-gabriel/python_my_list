from container.item import Item
from container.contains_interface import I_Contains
from place_state.place_state import Place_state_interface
from place_state.container_place_states import Container_empty_state


class Container(I_Contains): 
    item = Item()
    next_item = Item()
    place_state: Place_state_interface

    def __init__(self, item = None, place_state = Container_empty_state): 
        self.place_state = place_state(self)
        
        if item != None:
            self.append(item)
        else:
            self.item = None
        
        self.next_item = None

        self.index_place = 0

        
    def get_item(self):
        print('is in get item')
        print(self.item)
        return self.item

    def set_item(self, item):
        print('is here!!')
        print(item)
        self.item = item

    def get_next_item(self):
        return self.next_item
    
    def set_next_item(self, item):
        print('is here')
        print(item)
        self.next_item = item
        print(self.next_item)

    def append(self, item):
        self.place_state.append(item)
        """self.appended_items = 0
        match self.appended_items:
            case 0: self.item = item
            case 1: self.next_item = item
            case _: raise IndexError('Container can only hold 2 items')"""

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index > len(self):
            raise IndexError
        
        counter = 0
        for item in self:
            if counter == index:
                return item
            counter += 1

    def __setitem__(self, index, item):
        match index:
            case 0: return self.set_item(item)
            case 1: return self.set_next_item(item)
            case _: raise IndexError

    def __add__(self, item):
        self.append(item)

    def __repr__(self):
        representation = ''
        for item in self:
            print(f'item: {item}')
            representation += str(item) + ', '    
        representation = representation[:-2]
        return representation
    
    def __iter__(self):
        self.index_place = 0 
        return self
    
    def __next__(self):
        return self.place_state.__next__()

        """self.index += 1
        match self.test_index:
            case 1: return self.item
            case 2: return self.next_item
            case _: 
                self.index = 0
                raise StopIteration"""
    
    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length 
        
    def set_state(self, state):
        self.place_state = state

    def get_index_place_keeper(self):
        return self.index_place

    def set_index_place_keeper(self, place):
        self.index_place = place

def main():
    a = Container()
    a + 1
    print(a)
    a + 2
    print(a)
    print(a[0])
    print(a[1])
    a[1] = 5

    print(a)
    a + 3

if __name__ == '__main__':
    main()