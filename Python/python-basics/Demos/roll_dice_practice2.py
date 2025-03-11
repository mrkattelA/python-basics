import math
import random

def roll_dice(side=6):
    rolled_number = random.randint(1,side)
    return rolled_number

def main():
    side = 6
    total = 0

    num_rolls = 1
    roll = roll_dice(side)
    print("you rolled the number: ", roll)
    total += roll
    print("The total afer ",num_rolls, " roll is: ", total)

    num_rolls += 1
    roll = roll_dice(side)
    print("you rolled the second number is: ", roll)
    total += roll
    print ("The total after ", num_rolls, " roll is: ", total)

    num_rolls +=1
    roll = roll_dice(side)
    print("you rolled the number: ", roll)
    total += roll
    print("The total after ", num_rolls, " roll is: ", total)

    average = round(total/num_rolls, 2)
    print("you have rolled the average of: ", average, " per roll.")

    print("Thanks for playing")

main()