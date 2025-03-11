def list_basic():
    dice_roll = []
    for a in range(1, 7):
        for b in range(a, 7):
            roll = (a, b)
            dice_roll.append(roll)
    print(dice_roll)

def list_advance():
    dice_roll = [
        (a, b)
        for a in range(1, 7)
        for b in range(a, 7)
    ]
    print(dice_roll)

def main():
    list_advance()

main()
    