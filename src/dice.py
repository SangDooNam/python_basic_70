from singleton_decorator import singleton
import random


@singleton
class Dice:
    def __init__(self):
        self.number_of_rolls = 0
        self.record = {}
        self.last_roll = 0
        for i in range(1, 7):
            self.record[str(i)] = 0, 0.00

    # complete this method
    def roll(self):
        roll = -1
        return roll

    def __str__(self):
        return str(self.record)

