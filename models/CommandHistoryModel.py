class CommandHistoryModel:
    #contructor, se esta inicializando c v
    def __init__(self, command):
        self.command = command

    
    #getters and setters
    def get_command(self):
        return self.command
    
    def set_command(self, command):
        self.command = command
    
