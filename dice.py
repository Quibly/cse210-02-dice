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
        dice.first_dice = random.randint(1,6)
        dice.second_dice = random.randint(1,6)
        dice.third_dice = random.randint(1,6)
        dice.fourth_dice = random.randint(1,6)
        dice.fifth_dice = random.randint(1,6)
    def show_all_dice(dice):
        #Method to display the results of the dice roll
        print(f'{dice.first_dice} {dice.second_dice} {dice.third_dice} {dice.fourth_dice} {dice.fifth_dice}')


class Score:
    pass
