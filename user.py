from password import Password
from container import Container
class User:
    def __init__(self, username: str, psw: str, points=0) -> None:
        self.username = username
        self.password = Password(psw)
        self.points = points
        self.container = Container()
    
    def log_in(self):
        pass

    def log_out(self):
        pass

    def earn_points(self):
        pass

    def lose_points(self):
        pass

    def get_container(self) -> Container:
        return self.container
    
    def get_username(self) -> str:
        return self.username
    
    def get_password(self) -> str:
        return self.password.psw