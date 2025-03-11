phrase_num2 = 0
phrase_num = 0

def phrase():
    phrase = input("Choose your phrase: ")
    print(" Your phrase is: ", "'",phrase, "'", sep="")
    phrase_num = int(input("which character [Enter number]: "))
    phrase_num2 = phrase_num - 1
    character = phrase[phrase_num2]
    print("character ", phrase_num, " is ", character, ".", sep="")

def main():
    phrase()

main()
