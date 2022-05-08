from password import Password
from container import Container
class User:
    def __init__(self, user_id: int, username: str, psw: str, points=0) -> None:
        self.__user_id = user_id
        self.__username = username
        self.__password = Password(psw)
        self.__points = points
        self.__container = Container()
    
    def earn_points(self, points: int) -> None:
        self.__points += points

    def lose_points(self, points: int) -> None:
        if self.points > 0:
            self.__points -= points

    @property
    def container(self) -> Container:
        return self.__container
    
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