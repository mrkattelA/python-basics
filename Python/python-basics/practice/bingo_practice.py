import random

def bingo():
    balls = {
        "B" : list(range(1,16)),
        "I" : list(range(16,31)),
        "N" : list(range(31,46)),
        "G" : list(range(46,51)),
        "O" : list(range(51,66)),
    }

    while balls:
        letter = random.choice(list(balls.keys()))
        number = random.choice(balls[letter])
        balls[letter].remove(number)
        if not balls:
            print("Removing", letter)
            del balls[letter]
        yield (letter, number)

def main():
    for ball in bingo():
        print(ball)
        if input("Enter for next ball or 'q' to quite: ") == "q":
            print("Goodbye! ")
            break
    else:
        print("All out of balls. ")

main()