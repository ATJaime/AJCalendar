from item import Item
class Meeting(Item):
    def__init__(self,link: str, meeting_date: date, description: str, creation_date: date, relevance_level: int) -> None:
        super.__init__(description: str, creation_date: date, relevence_level: int)
        
        self.link = link
        self.meeting_date = meeting_date
    
    def cancel_meeting(self) -> None:
        pass
