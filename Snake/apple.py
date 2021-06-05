import random
from config import Config


class Apple():
    def __init__(self):
        self.setNewLocation()

    def setNewLocation(self):
        self.x = random.ranint(0, Config.CELLWIDTH-1)
        self.y = random.ranint(0, Config.CELLHEIGHT-1)
