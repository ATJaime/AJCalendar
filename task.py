from datetime import date
from datetime import datetime
from item import Item
class Task(Item):
    def __init__(
        self,
        name: str,
        description: str, 
        relevance_level: int,  
        due_date: date, 
        is_done: bool = False
    )-> None:
        self.__name = name
        self.__description = description
        self.__relevance_level = relevance_level
        self.__creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
        self.__due_date = due_date
        self.__is_done = is_done
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def state(self) -> bool:
        return self.__is_done

    @property
    def due_date(self) -> date:
        return self.__due_date
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def relevance_level(self) -> int:
        return self.__relevance_level

    @property
    def creation_date(self) -> date:
        return self.__creation_date
    
    @state.setter
    def state(self, new_state: bool) -> None:
        self.__is_done = new_state
    
    @due_date.setter
    def due_date(self, due_date: date) -> None:
        self.__due_date = due_date
    
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name
    
    @description.setter
    def description(self, new_description: str) -> None:
        self.__description = new_description

    @relevance_level.setter
    def relevance_level(self, relevance_level: int) -> None:
        self.__relevance_level = relevance_level
    
    @creation_date.setter
    def creation_date(self, date: date) -> date:
        self.__creation_date = date