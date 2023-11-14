from singleton_decorator import singleton
from game_factory import GameFactory


@singleton
class GameMaster:
    def __init__(self):
        self.credit = 100

    def host_game(self, game_type):
        # complete this method
        game_start = GameFactory()
        result = game_start.create_object(game_type)
        self.credit = self.credit - result
        

    def __str__(self):
        return f"Game Master capital: {self.credit}"



