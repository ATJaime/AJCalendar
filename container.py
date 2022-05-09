from task import Task
from note import Note
from meeting import Meeting
from datetime import date

class Container():
    def __init__(self):
        self.__notes = []
        self.__tasks = []
        self.__meetings = []
    
    def create_task(
            self,
            name: str, 
            description: str, 
            relevance_level: int,
            due_date: date,
            is_done: bool
    ) -> None:
        self.__tasks.append(Task(
            name=name, 
            description=description, 
            relevance_level=relevance_level,
            due_date=due_date, 
            is_done=is_done
            )
        )

    def create_meeting(
            self,
            name: str, 
            description: str,
            relevance_level: int,
            link: str,
            meeting_date: date
    ) -> None:
        self.__meetings.append(Meeting(
            name=name, description=description, 
            relevance_level=relevance_level,
            link=link, meeting_date=meeting_date
            )
        )
    
    def create_note(
            self, name: str,
            description: str,
            relevance_level: int,
            font: str,
            font_size: float
    ) -> None:
        self.__notes.append(Note(
            name=name, description=description, 
            relevance_level=relevance_level,
            font=font, font_size=font_size
            )
        )
    
    def block_distractions(self):
        pass
    
    def remove_task(self, index: int):
        self.__tasks.remove[index]
    
    def remove_meeting(self, index: int):
        self.__meetings.remove[index]
    
    def remove_note(self, index: int):
        self.__notes.remove[index]
    
    @property
    def notes(self) -> list:
        return self.__notes
    
    @property
    def tasks(self) -> list:
        return self.__tasks
    
    @property
    def meetings(self) -> list:
        return self.__meetings

    def unblock_distractions(self):
        pass
    
    def update_preferences(self):
        pass
