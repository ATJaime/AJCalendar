from password import Password
from note import Note
from task import Task
from meeting import Meeting
from datetime import date
class User:
    def __init__(self, user_id: int, username: str, psw: str, points=0) -> None:
        self.__user_id = user_id
        self.__username = username
        self.__password = Password(psw)
        self.__points = points
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
    
    def remove_task(self, task: Task):
        self.__tasks.remove(task)
    
    def remove_meeting(self, meeting: Meeting):
        self.__meetings.remove(meeting)
    
    def remove_note(self, note: Note):
        self.__notes.remove(note)
    
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def password(self) -> str:
        return self.__password.psw
    
    @property
    def points(self) -> int:
        return self.__points
    
    @property
    def user_id(self) -> int:
        return self.__user_id
    
    @property
    def notes(self) -> list:
        return self.__notes
    
    @property
    def tasks(self) -> list:
        return self.__tasks
    
    @property
    def meetings(self) -> list:
        return self.__meetings

    @username.setter
    def username(self, username: str) -> None:
        self.__username = username
    
    @password.setter
    def password(self, password: str) -> None:
        self.__password.update(password)

    def unblock_distractions(self):
        pass
    
    def update_preferences(self):
        pass
    
    def earn_points(self, points: int) -> None:
        self.__points += points

    def lose_points(self, points: int) -> None:
        if self.points > 0:
            self.__points -= points