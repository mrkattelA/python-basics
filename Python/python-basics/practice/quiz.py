print("Welcome to quiz game:")

def main():
    score = 0
    games  = input("Do you want to play quiz game? ")
    if games.lower() != "yes":
        quit()
    print ("Okay Lets play the game! ")

    answer = input("what is USA stands for? ")
    if answer.title() == "United States Of America":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer = input("what is UK stands for? ")
    if answer.title() == "United Kingdom":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer = input("what is MD stands for? ")
    if answer.title() == "Maryland":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    answer = input("what is CA stands for? ")
    if answer.title() == "California":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print("your make ", score, "question correct. ")
    print("you score ", (score/4)*100,"%")

main()