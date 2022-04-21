from modify import Modify
from task import Task
from note import Note
from meeting import Meeting
class Container(Modify):
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
