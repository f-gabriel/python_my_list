from Multicontainer import Multicontainer as MC


class My_List(MC):
    def __init__(self, value = None):
        super().__init__(value, '[]')
            
    def get_values(self):
        print('is here')
        next: My_List = super().__next__()
        return next.get_value()
    
    def __add__(self, other: MC):
        for item in other:
            self.add(item)

    

    def sort():
        pass