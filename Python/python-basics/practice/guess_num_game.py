import random

def guess_num(nums):
    return nums.isdigit() and 1 <= int(nums) <= 100

def main():
    computer_number = random.randint(1,100)

    user_number = False
    

    print("Let's Play the number guessing game. ")
    enter_nums = input("Guess the number from 0 to 100: ")

    guess_attempt = 0

    while not user_number:
        if not guess_num(enter_nums):
            print("I will not count the entered number. ")
            enter_nums = input("Please Enter the valid number between 1 and 100: ")
        else: 
            enter_nums = int(enter_nums)
            guess_attempt += 1
            if enter_nums > computer_number:
                enter_nums = input(f"It is a smaller than {enter_nums}. Enter again: ")
            elif enter_nums < computer_number:
                enter_nums = input(f"It is higher number than {enter_nums}. Enter again: ")
            else:
                print(f"you guessed correct number in {guess_attempt} attempts.")
                user_number = True
                

            
    print("Thank you for playing! ")

main()