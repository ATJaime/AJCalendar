from item import Item
from datetime import date
from datetime import datetime
class Meeting(Item):
    def __init__(
            self,
            name: str,
            description: str, 
            relevance_level: int, 
            link: str, 
            meeting_date: date
    ) -> None:
        self.name = name
        self.description = description
        self.relevance_level = relevance_level
        self.creation_date = datetime.strftime(datetime.now(), '%b %d, %Y, %H:%M')
        self.link = link
        self.meeting_date = meeting_date
    
    def get_link(self) -> str:
        return self.link
    
    def get_meeting_date(self) -> date:
        return self.meeting_date

    def cancel_meeting(self) -> None:
        pass
