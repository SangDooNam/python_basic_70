from abc import ABC, abstractmethod
from dice import Dice


class Game(ABC):
    def __init__(self):
        self.gains = -10

    @abstractmethod
    def play_game(self):
        raise NotImplementedError()


class SumGame(Game):
    def play_game(self):
        # Complete this method
        return self.gains


class ParityGame(Game):
    def play_game(self):
        # Complete this method
        return self.gains

