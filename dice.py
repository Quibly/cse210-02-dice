"""
Dice.py - Dice is a game in which the player seeks to earn as many points as possible by repeatedly 
rolling five dice and accumulating the score until they are no longer able to continue.

Author: Adam Dutson
Course: CSE 210: Programming with Classes

The game is played with five dice.
The player is asked, "Roll dice?" at the beginning of each turn.
If the player answers "n" or no, the game is over.
If the player answers "y" or yes, the points are added to their score.
The player scores 100 points for each one that is rolled.
The player scores 50 points for each five that is rolled.
The dice values and player score are displayed on the screen.
If the player does not roll any ones or fives the game is over.
"""

import random

class Roll:
    # A class for producing roll results
    def __init__(dice):
        #Constructor to get random dice results for 5 dice
        dice.first_dice = ""
        dice.second_dice = ""
        dice.third_dice = ""
        dice.fourth_dice = ""
        dice.fifth_dice = ""

    def show_all_dice(dice):
        #Method to display the results of the dice roll
        print(f'You rolled: {dice.first_dice} {dice.second_dice} {dice.third_dice} {dice.fourth_dice} {dice.fifth_dice}')

class Scoring:
    # A class for determining results and scoring for the Roll results
    def __init__(dice, number):
        dice.number = number
        dice.score = int(0)

    def score_result(dice):
        if dice.number == 1:
            dice.score = 100
        elif dice.number == 5:
            dice.score = 50
        else:
            dice.score = 0

def main():
    roll_score = int(0)
    total_score = int(0)
    you_rolled = Roll()
    print()
    roll_dice = input('Roll dice? [y/n]: ')
    while roll_dice == 'y':
        #Generate random dice results and print results
        you_rolled.first_dice = random.randint(1,6)
        you_rolled.second_dice = random.randint(1,6)
        you_rolled.third_dice = random.randint(1,6)
        you_rolled.fourth_dice = random.randint(1,6)
        you_rolled.fifth_dice = random.randint(1,6)
        you_rolled.show_all_dice()
        roll_score = int(0)
        scoring = Scoring(you_rolled.first_dice)
        scoring.score_result()
        roll_score += scoring.score
        scoring = Scoring(you_rolled.second_dice)
        scoring.score_result()
        roll_score += scoring.score
        scoring = Scoring(you_rolled.third_dice)
        scoring.score_result()
        roll_score += scoring.score
        scoring = Scoring(you_rolled.fourth_dice)
        scoring.score_result()
        roll_score += scoring.score
        scoring = Scoring(you_rolled.fifth_dice)
        scoring.score_result()
        roll_score += scoring.score
        if roll_score != 0:
            total_score += roll_score
            print(f'Your score is: {total_score}')
            print()
            roll_dice = input('Roll dice? [y/n]: ')
        else:
            roll_dice = 'n'
            print('Your roll didn\'t score any points. The game is over.')
            print()

if __name__ == "__main__":
    main()