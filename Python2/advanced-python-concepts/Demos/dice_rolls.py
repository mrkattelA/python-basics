def list_basic():
    dice_rolls = []
    for a in range(1, 7):
        for b in range(1, 7):
            roll = (a, b)
            dice_rolls.append(roll)

    print(dice_rolls)

def list_advance():
    dice_rolls = [
        (a,b)
        for a in range(1,7)
        for b in range(1,7)
    ]

    print(dice_rolls)

def main():
    list_advance()

main()