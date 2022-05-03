from task import Task
from note import Note
from meeting import Meeting
from datetime import date

class Container():
    def __init__(self):
        self.notes = []
        self.tasks = []
        self.meetings = []
    
    def get_notes(self) -> list:
        return self.notes
    
    def get_tasks(self) -> list:
        return self.tasks
    
    def get_meetings(self) -> list:
        return self.meetings

    def create_task(
            self,
            name: str, 
            description: str, 
            relevance_level: int,
            due_date: date,
            is_done: bool
    ) -> None:
        self.tasks.append(Task(
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
        self.meetings.append(Meeting(
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
        self.notes.append(Note(
            name=name, description=description, 
            relevance_level=relevance_level,
            font=font, font_size=font_size
            )
        )
    
    def block_distractions(self):
        pass
    
    def remove_task(self):
        pass
    
    def remove_meeting(self):
        pass
    
    def remove_note(self):
        pass
    
    def unblock_distractions(self):
        pass
    
    def update_preferences(self):
        pass
