import math
import random

def roll_dice(side):
    side = random.randint(1,6)
    return side

def main():
    #roll_dice(1)
    #print("you rolled is: ", roll_dice(1))
    First_roll = roll_dice(1)
    print("The First roll is : " , First_roll)
    second_roll = roll_dice(2)
    print("The Second roll is : ", second_roll)
    third_roll = roll_dice(3)
    print("The Third roll is : ", third_roll)
    total1 = sum(First_roll + second_roll)
    print(total1)
    Total = First_roll + second_roll + third_roll
    print(Total)
    Average = Total/3
    print("the average of the three dice rolls is ",Average, ".", sep="")
    
main()