from datetime import date
from datetime import datetime
from item import Item
class Task(Item):
    def __init__(self,
        description: str, 
        relevance_level: int,  
        color: str, 
        due_date: date, 
        is_done: bool = False
    )-> None:
        super().__init__(description=description,  
            relevance_level=relevance_level,
            creation_date=datetime.now()
        )
        self.color = color
        self.due_date = due_date
        self.is_done = is_done
    
    def set_state(self, new_state: bool) -> None:
        self.is_done = new_state
    
    def set_relevance_level(self, relevance_level: int) -> None:
        self.relevance_level = relevance_level

    def set_color(self, color: str) -> None:
        self.color = color
    
    def set_due_date(self, due_date: date) -> None:
        self.due_date = due_date
