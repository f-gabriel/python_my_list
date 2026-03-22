from abc import ABC, abstractmethod

class I_Contains(ABC):
    @abstractmethod
    def get_value(self):
        pass
    @abstractmethod
    def set_value(self):
        pass
    @abstractmethod
    def get_next_value(self):
        pass
    @abstractmethod
    def set_next_value(self, item):
        pass
    @abstractmethod
    def append(self, item):
        pass