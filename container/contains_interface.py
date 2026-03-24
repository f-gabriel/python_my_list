from abc import ABC, abstractmethod

class I_Contains(ABC):
    @abstractmethod
    def get_item(self):
        pass
    @abstractmethod
    def set_item(self):
        pass
    @abstractmethod
    def get_next_item(self):
        pass
    @abstractmethod
    def set_next_item(self, item):
        pass
    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def set_state(self, state):
        pass
    @abstractmethod
    def get_index_place_keeper(self):
        pass
    @abstractmethod
    def set_index_place_keeper(self, place):
        pass
    
