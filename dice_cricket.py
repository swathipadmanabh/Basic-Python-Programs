import random

print("Welcome to Dice Cricket, Good luck")

dice_roll = 0
score = 0

while dice_roll != 5:
    user_in = input("Enter R to roll the dice or Q to quit the game").upper()
    if user_in == 'R':
        dice_roll = random.randint(1, 6)
        if dice_roll != 5:
            score += dice_roll
            print("the score you have rolled is", dice_roll, "and the total score is", score)
        else:
            print("Sorry, you have been declared out, better luck next time")
    elif user_in == 'Q':
        print("you have quit the game, see you soon")

print("*****************************GAME OVER ********************************")

