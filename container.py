from modify import Modify
from task import Task
from note import note
from meeting import Meeting
class Container(Modify):
    def __init__(self):
        self.notes = []
        self.tasks = []
        self.meetings = []
