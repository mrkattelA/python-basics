import random

def computer_option():
    options = ["rock", "paper","scissors"]
    x = random.choice(options)
    print("Computer :", x)

def main():
    (Rock, Paper, Scissor) = (1,2,3)
    User_input = input("1 for Rock, 2 for Paper, 3 for scissor: ")
    computer_option()
    print("User : ", User_input)
    
main()