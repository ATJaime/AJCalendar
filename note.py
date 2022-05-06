from item import Item
from datetime import datetime
class Note(Item):
    def __init__(
            self,
            name: str,
            description: str, 
            relevance_level: int,
            font: str, 
            font_size: float, 
    ) -> None:
        self.name = name
        self.description = description
        self.relevance_level = relevance_level
        self.creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
        self.font = font
        self.font_size = font_size
       
    def set_font(self, new_font: str) -> None:
        self.font = new_font
    
    def set_font_size(self, new_size: int) -> None:
        self.font_size = new_size
    
    def get_font(self) -> str:
        return self.font

    def get_font_size(self) -> None:
        return self.font_size
    