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

        dice = Dice()
        result = dice.roll() + dice.roll() + dice.roll() + dice.roll()
        if result == 16 or result == 17:
            self.gains += 10

        elif result >= 18:
            self.gains += 40

        elif result < 16:
            self.gains += 0

        return self.gains


class ParityGame(Game):
    def play_game(self):
        # Complete this method
        dice_1 = Dice().roll()
        dice_2 = Dice().roll()
        dice_3 = Dice().roll()
        if dice_1 == dice_2 == dice_3 and not bool(dice_1 % 2):
            self.gains += 50
            
        else:
            self.gains += 0
                    
        
        return self.gains


# a = SumGame()
# b = ParityGame()
# print(a.play_game())
# print(b.play_game())