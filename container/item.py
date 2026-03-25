import sys

sys.path.append('c:\\Users\\nilss\\OneDrive\\Skrivbord\\programering\\Python\\Projekt\\my_list\\python_my_list')

class Item():
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner = None):
        return getattr(instance, self.private_name)
    
    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)