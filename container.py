from item import Item
from contains_interface import I_Contains


class Container(I_Contains): 
    item = Item()
    next_item = Item()

    def __init__(self, item = None): 
        self.item = item
        self.next_item = None
        
    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def get_next_item(self):
        return self.next_item
    
    def set_next_item(self, item):
        self.next_item = item

    def append(self, item):
        self.appended_items = 0
        match self.appended_items:
            case 0: self.item = item
            case 1: self.next_item = item
            case _: raise IndexError('Container can only hold 2 items')

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
            representation += str(item) + ', '    
        representation = representation[:-2]
        return representation
    
    def __iter__(self):
        self.index = 0 
        return self
    
    def __next__(self):
        self.index += 1
        match self.test_index:
            case 1: return self.item
            case 2: return self.next_item
            case _: 
                self.index = 0
                raise StopIteration
    
    def __len__(self):
        try:
            return self.appended_items
        except AttributeError: 
            return 0
        


def main():
    a = Container()
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