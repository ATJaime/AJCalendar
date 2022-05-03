class Password:
    def __init__(self, psw: str) -> None:
        self.psw = psw
    
    def hide(self) -> None:
        pass
    
    def show(self) -> None:
        pass

    def update(self, new_psw: str) -> None:
        self.psw = new_psw

    def validate(self) -> None:
        pass