from password import Password
class User:
    def __init__(self, username: str, psw: str, points=0) -> None:
        self.username = username
        self.password = Password(psw)
        self.points = points
    
    def log_in(self):
        pass

    def log_out(self):
        pass

    def earn_points(self):
        pass

    def lose_points(self):
        pass