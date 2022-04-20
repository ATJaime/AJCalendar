from datetime import date
from item import Item
class Task(Item):
    def __init__(self, 
        is_done: bool = False, 
        color: str, 
        due_date: date, 
        description: str, 
        creation_date: date, 
        relevance_level: int
    )-> None:
        super.__init__(description=description, creation_date=creation_date, relevance_level=relevance_level)
        self.is_done = is_done
        self.color = color
        self.due_date = due_date
    
    def set_state(self, new_state: bool) -> None:
        self.is_done = new_state
    
    def set_relevance_level(self, relevance_level: int) -> None:
        self.relevance_level = relevance_level

    def set_color(self, color: str) -> None:
        self.color = color
    
    def set_due_date(self, due_date: date) -> None:
        self.due_date = due_date
