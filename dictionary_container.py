from my_container import Container
from abc import ABC, abstractmethod

class Dictionary_Interface(ABC):
    @abstractmethod
    def get_key(self):
        pass
    @abstractmethod
    def get_value(self):
        pass
    @abstractmethod
    def set_key(self):
        pass
    @abstractmethod
    def set_value(self):
        pass


class Key_Value(Container, Dictionary_Interface):
    def __init__(self, key, value = None):
        super().__init__(key)
        self.next_item = value

    def get_key(self):
        return self.item
    
    def set_key(self, key):
        self.item = key
    
    def get_value(self):
        return self.next_item
    
    def set_value(self, value):
        self.next_item = value
    
    def __repr__(self):
        key = str(self.get_key())
        value = str(self.get_value())
        return (f'{key}: {value}')
    
    
