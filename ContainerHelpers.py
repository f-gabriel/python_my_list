from container_interfaces import I_Has_Iterator as IHI

class Container_Itterator(IHI):
    def __init__(self, user_object: IHI):
        self.user_object = user_object
        self.next_return = user_object
    
    def get_next_value(self):
        #input('is here 3')
        if self.next_return != None:
            #input("is here 1")
            
            current_return = self.next_return
            
            self.next_return = self.next_return.next_value
            #print('is before return')
            return current_return
        else:
            self.next_return = self.user_object
            #print('is here 1')
            #input('is here 2')
            raise IndexError
        
    def set_next_value(self, multicontainer: IHI):
        self.next_return = multicontainer

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            #print('is in try')
            return self.get_next_value()
        except IndexError:
            #print('is in except')
            raise StopIteration
        


class String_Representation:
    def __init__(self, user_object, brackets: str):
        self.user_object = user_object
        self.brackets = brackets
        
    def get_collection_string_representation(self):
        return_string = ''
        print('is in SR before for loop')
        for item in self.user_object:
            #print('is in SR for loop')
            return_string = return_string + ', ' + str(item)
        return return_string[2:]

    def add_class_specific_brackets(self, string):
        return self.brackets[0] + string + self.brackets[1]
    
    def string_representation(self):
        return_string = self.get_collection_string_representation()
        return_string = self.add_class_specific_brackets(return_string)
        return return_string