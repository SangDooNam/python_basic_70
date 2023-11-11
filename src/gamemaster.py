from singleton_decorator import singleton
from game_factory import GameFactory


@singleton
class GameMaster:
    def __init__(self):
        self.credit = 100

    def host_game(self, game_type):
        # complete this method
        pass

    def __str__(self):
        return f"Game Master capital: {self.credit}"



