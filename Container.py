from value import Value
from contains_interface import I_Contains


class Container(I_Contains): 
    value = Value()
    next_value = Value()

    def __init__(self, value = None, is_first_append = True):
        self.value = value
        self.next_value = None
        
    def get_value(self):
        return self.value

    def set_value(self, item):
        self.value = item

    def get_next_value(self):
        return self.next_value
    
    def set_next_value(self, item):
        self.next_value = item

    def append(self, item):
        self.appended_items = 0
        match self.appended_items:
            case 0: self.value = item
            case 1: self.next_value = item
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

    def __setitem__(self, index, value):
        match index:
            case 0: return self.set_value(value)
            case 1: return self.set_next_value(value)
            case _: raise IndexError

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
            case 1: return self.value
            case 2: return self.next_value
            case _: 
                self.test_index = 0
                raise StopIteration
    
    def __len__(self):
        return 2
        


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