class GiveClass:
    def give(self):
        return self
    
    def you(self):
        return Never()

class Never:
    Gonna = None
    def __init__(self):
        self.Gonna = GiveClass()
    
    def up(self):
        print("sussy baka")

class RickRoll(Never):
    def __init__(self) -> None:
        super().__init__()
    
    def Never(self):
        return Never()

# How to use?
# RickRoll().Never().Gonna.give().you().up()
