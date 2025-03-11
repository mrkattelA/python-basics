import random

def main():
    list_option = ["Rock", "Paper", "Scissors"]
    computer_random = random.choice(list_option)
    user_option = int(input("Press 1 for Rock, 2 for Paper, 3 for Scissors: "))-1
    print("Computer: ", computer_random)
    print("User: ", list_option[user_option])

main()
