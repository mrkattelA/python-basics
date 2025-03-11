def main():
    phrase = input("Enter your word here: ")
    print("you have entered : ", "'", phrase ,"'")
    first_num = int(input("Enter your first number: "))-1
    second_num = int(input("Enter your second number: "))
    phrase_slicing = phrase[first_num:second_num]
    print("your substring is : " , phrase_slicing)

main()