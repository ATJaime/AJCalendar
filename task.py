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
        self.name = name
        self.description = description
        self.relevance_level = relevance_level
        self.creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
        self.due_date = due_date
        self.is_done = is_done
    
    def __str__(self) -> str:
        return self.name
    
    def set_state(self, new_state: bool) -> None:
        self.is_done = new_state
    
    def set_due_date(self, due_date: date) -> None:
        self.due_date = due_date
    
    def get_state(self) -> bool:
        return self.is_done

    def get_due_date(self) -> date:
        return self.due_date

    def get_info(self) -> list:
        return[
            self.name,
            self.description, 
            self.relevance_level, 
            self.creation_date, 
            self.due_date, 
            self.is_done
        ]

    def set_name(self, new_name: str) -> None:
        self.name = new_name
    
    def set_description(self, new_description: str) -> None:
        self.description = new_description

    def set_relevance_level(self, relevance_level: int) -> None:
        self.relevance_level = relevance_level
    
    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_relevance_level(self) -> int:
        return self.relevance_level

    def get_creation_date(self) -> date:
        return self.creation_date