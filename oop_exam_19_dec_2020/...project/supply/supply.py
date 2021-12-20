from abc import abstractmethod, ABC

from project.survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self, value: int):
        self.needs_increase = value
    
    @property
    def needs_increase(self):
        return self.__needs_increase
    
    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zaero.")
        self.__needs_increase = value

    def apply(self, survivor: Survivor):
        survivor.needs = survivor.needs + self.needs_increase