from item import Item
from datetime import datetime
from datetime import date
class Note(Item):
    def __init__(
            self,
            name: str,
            description: str, 
            relevance_level: int,
            font: str, 
            font_size: float, 
    ) -> None:
        self.__name = name
        self.__description = description
        self.__relevance_level = relevance_level
        self.__creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
        self.__font = font
        self.__font_size = font_size
    
    @property
    def font(self) -> str:
        return self.__font

    @property
    def font_size(self) -> None:
        return self.__font_size
    
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
    
    @font.setter
    def font(self, new_font: str) -> None:
        self.__font = new_font
    
    @font_size.setter
    def font_size(self, new_size: int) -> None:
        self.__font_size = new_size
    
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