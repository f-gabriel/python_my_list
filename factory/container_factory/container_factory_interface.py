from abc import ABC, abstractmethod
from container.contains_interface import I_Contains


class I_container_factory(ABC):
    @abstractmethod
    def make_container(self):
        pass
    @abstractmethod
    def make_place_state(self):
        pass





















"""from contains_interface import I_Contains
from container import Container
from containers import Containers
from my_list import My_List
from my_dictionary import My_Dictionary
from dictionary_container import Key_Value

from place_state.place_state import Place_state_interface



class Container_factory():
    def create_container(self, container_type: I_Contains, place_state_type: Place_state_interface, item = None):
        new_container: I_Contains = container_type.__class__(item)
        new_place_state: Place_state_interface = place_state_type.__class__(new_container)
        new_container.set_state(new_place_state)
        return new_container
    
    def create_container(self, container_type: I_Contains, place_state_type: Place_state_interface, item = None, first_container = None):
        new_container: I_Contains = container_type.__class__(item)
        new_place_state: Place_state_interface = place_state_type.__class__(new_container, first_container)
        new_container.set_state(new_place_state)
        return new_container
"""