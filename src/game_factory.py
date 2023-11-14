from game import ParityGame, SumGame


class GameFactory:
    @staticmethod
    def create_object(game_type):
        # Complete this method
        if game_type == 'parity':
            return ParityGame().play_game()
        elif game_type == 'sum':
            return SumGame().play_game()
        raise TypeError('Invalid argument')

