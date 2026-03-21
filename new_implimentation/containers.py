from new_container import *
from container_implementation import *

class Containers(New_Container): # kanske vill ha attribut för om detta är huvud-containern
    implementation: C_Implementation_Interface
    next_value: Containers
    

    def __init__(self, value = None, implementation = Main_C_Implementation):
        super().__init__(value)
        self.implementation = implementation(self)
        #self.implementation.add_owner(self)
        
    
    def append(self, item):
        #print(item)
        self.implementation.append(item)
        #new_item = item
        #if self.value == None:
        #    super().append(new_item)
        #    return
        #if self.is_main_container:
        #    new_item = Containers(item, is_main_container=False)
        #try: 
        #    super().append(new_item)
        #except IndexError:
        #    self.next_value.append(new_item)

    def __repr__(self):
        representation = ''
        for value in self:
            if value != None:
                print('is in repr')
                input(value.value)
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
    a + 1
    a + 2
    a + 3
    a + 'strumpa'
    #a + a
    print(a) 
    #print(len(a))

if __name__ == '__main__':
    main()