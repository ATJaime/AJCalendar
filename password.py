from werkzeug.security import generate_password_hash
class Password:
    def __init__(self, psw: str) -> None:
        self.psw = psw
        self.encrypt()
    
    def encrypt(self) -> None:
        self.psw = generate_password_hash(self.psw)
    
    def update(self, new_psw: str) -> None:
        self.psw = new_psw
        self.encrypt()
        