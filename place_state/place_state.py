from abc import ABC, abstractmethod
from container.contains_interface import I_Contains

class Place_state_interface(ABC):
    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def __next__(self):
        pass

class Place_state(Place_state_interface):
    owner: I_Contains

    def __init__(self, owner):
        self.owner = owner

    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def __next__(self):
        pass
