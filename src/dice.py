from singleton_decorator import singleton
import random


@singleton
class Dice:
    def __init__(self):
        self.number_of_rolls = 0
        self.occurrences_of_one = 0
        self.occurrences_of_two = 0
        self.occurrences_of_three = 0
        self.occurrences_of_four = 0
        self.occurrences_of_five = 0
        self.occurrences_of_six = 0
        self.record = {}
        self.last_roll = 0
        for i in range(1, 7):
            self.record[str(i)] = 0, 0.00

    # complete this method
    def roll(self):
        roll = random.randint(1, 6)
        if roll == 1:
            self.occurrences_of_one += 1
        elif roll == 2:
            self.occurrences_of_two += 1
        elif roll == 3:
            self.occurrences_of_three += 1
        elif roll == 4:
            self.occurrences_of_four += 1
        elif roll == 5:
            self.occurrences_of_five += 1
        elif roll == 6:
            self.occurrences_of_six += 1
        self.number_of_rolls += 1
        self.record["1"] = self.occurrences_of_one, round(
            self.occurrences_of_one / self.number_of_rolls, 2
        )
        self.record["2"] = self.occurrences_of_two, round(
            self.occurrences_of_two / self.number_of_rolls, 2
        )
        self.record["3"] = self.occurrences_of_three, round(
            self.occurrences_of_three / self.number_of_rolls, 2
        )
        self.record["4"] = self.occurrences_of_four, round(
            self.occurrences_of_four / self.number_of_rolls, 2
        )
        self.record["5"] = self.occurrences_of_five, round(
            self.occurrences_of_five / self.number_of_rolls, 2
        )
        self.record["6"] = self.occurrences_of_six, round(
            self.occurrences_of_six / self.number_of_rolls, 2
        )
        return roll

    def __str__(self):
        return str(self.record)


# dice = Dice()

# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice.roll())
# print(dice.number_of_rolls)
# print(dice.record)
# print(dice)
