from container_interfaces import *
from container import *

class Container_Itterator(I_Has_Iterator):
    def __init__(self, user_object: I_Has_Iterator):
        self.user_object: Container = user_object
        self.next_return: Container = user_object
    
    def get_next_value(self):
        if self.next_return != None:
            current_return = self.next_return
            self.next_return = self.next_return.next_value
            return current_return
        else:
            self.next_return = self.user_object
            raise IndexError
        
    def set_next_value(self, multicontainer: I_Has_Iterator):
        self.next_return = multicontainer

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return self.get_next_value()
        except IndexError:
            raise StopIteration
        

class String_Representation(Has_string_representation):
    def __init__(self, user_object, brackets: str):
        self.user_object = user_object
        self.brackets = brackets
        
    def string_representation(self):
        return_string = self.get_collection_string_representation()
        return_string = self.add_class_specific_brackets(return_string)
        return return_string

    def get_collection_string_representation(self):
        return_string = ''
        item: Container
        for item in self.user_object:
            return_string = return_string + ', ' + str(item.get_value())
        return return_string[2:]

    def add_class_specific_brackets(self, string):
        return self.brackets[0] + string + self.brackets[1]
    
    