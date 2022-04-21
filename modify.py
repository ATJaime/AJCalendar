from datetime import date
from task import Task
from meeting import Meeting
from note import Note
class Modify:
    def create_task(self, 
        description: str, 
        relevance_level: int,
        color: str,
        due_date: date,
        is_done: bool
    ) -> None:
        self.tasks.append(Task(
            description=description, relevance_level=relevance_level,
            color=color, due_date=due_date, is_done=is_done
            )
        )

    def create_meeting(self):
        pass
    
    def create_note(self):
        pass
    
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
