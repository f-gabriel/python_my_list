import sys

sys.path.append('c:\\Users\\nilss\\OneDrive\\Skrivbord\\programering\\Python\\Projekt\\my_list\\python_my_list')

from abc import ABC, abstractmethod
#import container.contains_interface as CI

class Place_state_interface(ABC):
    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def __next__(self):
        pass

class Place_state(Place_state_interface):
    #owner: CI.I_Contains

    def __init__(self, owner):
        self.owner = owner

    @abstractmethod
    def append(self, item):
        pass
    @abstractmethod
    def __next__(self):
        pass
