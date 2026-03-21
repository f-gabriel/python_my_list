from abc import ABC, abstractmethod

class I_Has_Iterator(ABC):
    @abstractmethod
    def get_next_value():
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class Has_string_representation(ABC):
    ...
