from password import Password
from container import Container
class User:
    def __init__(self, username: str, psw: str, points=0) -> None:
        self.username = username
        self.password = Password(psw)
        self.points = points
        self.container = Container()
    
    def earn_points(self, points: int) -> None:
        self.points += points

    def lose_points(self, points: int) -> None:
        if self.points > 0:
            self.points -= points

    def get_container(self) -> Container:
        return self.container
    
    def get_username(self) -> str:
        return self.username
    
    def get_password(self) -> str:
        return self.password.psw
    
    def get_points(self) -> int:
        return self.points