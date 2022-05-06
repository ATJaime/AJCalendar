from datetime import date
from datetime import datetime
from abc import ABC
from abc import abstractmethod
class Item(ABC):

    @abstractmethod
    def __init__(
            self, 
            name: str, 
            description: str, 
            relevance_level: int
    ) -> None:
        self.name = name
        self.description = description
        self.relevance_level = relevance_level
        self.creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
    
    @abstractmethod
    def set_name(self, new_name: str) -> None:
        self.name = new_name
    
    @abstractmethod
    def set_description(self, new_description: str) -> None:
        self.description = new_description

    @abstractmethod
    def set_relevance_level(self, relevance_level: int) -> None:
        self.relevance_level = relevance_level
    
    @abstractmethod
    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def get_relevance_level(self) -> int:
        return self.relevance_level

    @abstractmethod
    def get_creation_date(self) -> date:
        return self.creation_date