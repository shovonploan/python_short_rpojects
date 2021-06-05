class Error (Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message=message
class SlotError(Error):
    def __init__(self,message):
        self.message=message
