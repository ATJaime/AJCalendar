from item import Item
from datetime import date
class Meeting(Item):
    def __init__(self, 
        link: str, 
        meeting_date: date, 
        description: str, 
        creation_date: date, 
        relevance_level: int
    ) -> None:
        super.__init__(description=description,
            creation_date=creation_date,
            relevance_level=relevance_level
        )
        self.link = link
        self.meeting_date = meeting_date
    
    def cancel_meeting(self) -> None
        pass
