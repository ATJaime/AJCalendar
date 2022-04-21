from datetime import date
from item import Item
class Note(Item):
    def __init__(self,
        font: str, 
        font_size: float, 
        font_color:  str, 
        background_color: str,
        description: str, 
        creation_date: date, 
        relevance_level: int
    ) -> None:
        super().__init__(description=description, 
            creation_date=creation_date, 
            relevance_level=relevance_level
        )
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
       
    def set_font(self) ->None:
        pass
    
    def set_font_size(self) -> None:
        pass
    
    def set_font_color(self) -> None:
        pass
    
    def set_background_color(self) -> None:
        pass
