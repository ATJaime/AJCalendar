from item import Item
from datetime import date
from datetime import datetime
import webbrowser
class Meeting(Item):
    def __init__(
            self,
            name: str,
            description: str, 
            relevance_level: str, 
            link: str, 
            meeting_date: date
    ) -> None:
        self.__name = name
        self.__description = description
        self.__relevance_level = relevance_level
        self.__creation_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        self.__link = link
        self.__meeting_date = meeting_date
    
    def __str__(self) -> str:
        return self.__name

    @property
    def link(self) -> str:
        return self.__link
    
    @property
    def meeting_date(self) -> date:
        return self.__meeting_date
    
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
    
    @meeting_date.setter
    def meeting_date(self, meeting_date: date) -> None:
        self.__meeting_date = meeting_date

    @link.setter
    def link(self, link: str) -> None:
        self.__link = link
    
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
    
    def open_meeting(self) -> None:
        webbrowser.open(self.link)