from datetime import date
from abc import ABC
from abc import abstractmethod
class Item(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def relevance_level(self) -> int:
        ...

    @property
    @abstractmethod
    def creation_date(self) -> date:
        ...
    
    @name.setter
    @abstractmethod
    def name(self, new_name: str) -> None:
        ...
    
    @description.setter
    @abstractmethod
    def description(self, new_description: str) -> None:
        ...

    @relevance_level.setter
    @abstractmethod
    def relevance_level(self, relevance_level: int) -> None:
        ...